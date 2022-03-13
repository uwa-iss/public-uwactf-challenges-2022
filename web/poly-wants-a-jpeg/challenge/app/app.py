from flask import Flask, request, g, session
from urllib.parse import urlparse
from PIL import Image, ImageFile
from werkzeug.exceptions import HTTPException
import sqlite3, os, json, argparse, bcrypt, logging, glob


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY").encode()

app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config['UPLOAD_URL_FOLDER'] = os.getenv("UPLOAD_URL_FOLDER")
app.config['UPLOAD_HTML_FOLDER'] = os.getenv("UPLOAD_HTML_FOLDER")
app.config['UPLOAD_REL_HTML_FOLDER'] = os.getenv("UPLOAD_REL_HTML_FOLDER")
app.config['POLY_PASSWORD'] = os.getenv("POLY_PASSWORD")
app.config['FLAG'] = os.getenv("FLAG")
logging.basicConfig(level=logging.INFO)

# Shouldn't discriminate uploaded JPEG files, even if they are slightly corrupted
ImageFile.LOAD_TRUNCATED_IMAGES = True


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect(os.getenv("DATABASE"))
    db.row_factory = make_dicts
    return db


def init_db():
    init_script = """
    CREATE TABLE IF NOT EXISTS "poly-images" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "from" VARCHAR,
        "path" VARCHAR
    );

    CREATE TABLE IF NOT EXISTS "users" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "username" VARCHAR,
        "password" VARCHAR
    );
    """

    with app.app_context():
        db = get_db()
        db.cursor().executescript(init_script)
        db.commit()

    # poly_password = os.urandom(32).hex()
    poly_password = app.config["POLY_PASSWORD"]
    logging.info("Poly's password is {}".format(poly_password))
    insert_db('INSERT INTO users ("username", "password") VALUES (?, ?)', args=("poly", bcrypt.hashpw(poly_password.encode(), bcrypt.gensalt())))


def query_db(query: str, args: tuple = (), one: bool = False):
    with app.app_context():
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(query: str, args: tuple = ()):
    with app.app_context():
        db = get_db()
        db.cursor().execute(query, args)
        db.commit()

def clear_uploads():
    def _del_folder(pattern):
        for file_str in glob.glob(pattern, recursive=False):
            if not os.path.isfile(file_str):
                continue

            os.remove(file_str)

    insert_db('DELETE FROM "poly-images"')

    _del_folder(app.config['UPLOAD_FOLDER'] + '/*')
    _del_folder(app.config['UPLOAD_HTML_FOLDER'] + '/*')

def json_response(data, status="success", status_code=200):
    response = {
        "status" : status,
        "value" : data
    }

    return app.response_class(
        response = json.dumps(response),
        status = status_code,
        mimetype = "application/json"
    )

def api_error(msg, status_code=404):
    return json_response(msg, status = "error", status_code = status_code)

def validate_url(url: str):
    try:
        parse_result = urlparse(url)
    except Exception:
        raise Exception("Invalid url was provided! 😡")
    if not parse_result.scheme == "http" and not parse_result.scheme == "https":
        raise Exception("Invalid scheme for url was provided! 😡")

def login_check(user_session: session):
    return "username" in user_session

def create_page(html_path: str, uploaded_by: str, url_path: str):
    # I can't be stuffed writing javascript code for poly. This is just way more convenient.
    # The JPEGS don't need to be hidden from others so leave it as a prize for others to find.
    template = """
    <html>
        <head>
            <title>Poly's Website</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="/css/main.css" />
        </head>

        <body>
            <section>
                <div id="grid-item">
                    <h3 style="color: rgb(21, 255, 0);">JPEG submitted by {uploaded_by}</h1>
                </div>
                <div id="grid-item">
                    <img src="{url_path}" />
                </div>
            </section>

            <div id="parrot-bg"></div>
            <script src="/js/jquery-3.6.0.min.js"></script>
            <script src="/js/jquery.notifyBar.js"></script>
            <script src="/js/main.js"></script>
        </body>
    </html>
    """.format(uploaded_by = uploaded_by, url_path = url_path)

    with open(html_path, 'w') as f:
        f.write(template)

@app.teardown_appcontext
def close_connection(exception: Exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.errorhandler(Exception)
def endpoint_not_found(e):
    if isinstance(e, HTTPException):
        e: HTTPException = e
        return api_error(e.description, e.code)
    return api_error("You broke something! ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾", 500)


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if not isinstance(username, str):
        return api_error("Missing username!", status_code=403)

    if not isinstance(password, str):
        return api_error("Missing password!", status_code=403)

    hashed_pw = query_db("SELECT password FROM users WHERE username = ?", args=(username,), one=True).get("password", None)

    if not isinstance(hashed_pw, bytes):
        return api_error("Incorrect username or password! 😲", status_code=401)

    if bcrypt.checkpw(password.encode(), hashed_pw):
        session["username"] = username
        return json_response({"redirect" : "/dashboard.html", "msg" : "Login was successful!"}, status_code=200)

    return api_error("Incorrect username or password! 😲", status_code=401)

@app.route("/api/flag", methods = ["GET"])
def get_flag():
    if not login_check(session):
        return api_error("You are not allowed here! 😡", status_code=401)

    return json_response(app.config["FLAG"])

@app.route("/api/jpegs/list", methods = ["GET"])
def list_jpegs():
    if not login_check(session):
        return api_error("You are not allowed here! 😡", status_code=401)

    jpegs = query_db('SELECT "from", "path" FROM "poly-images"')
    return json_response(jpegs)

@app.route("/api/jpegs/submit", methods = ["POST"])
def submit_jpegs():
    if 'file' not in request.files:
        return api_error("No file was sent!", status_code=400)

    if 'name' not in request.args:
        return api_error("We want to know who gave Poly this nice JPEG!", status_code=400)

    uploaded = request.files['file']
    try:
        image = Image.open(uploaded.stream)
        if not image.format == "JPEG":
            raise Exception("Not a JPEG")
    except Exception:
        return api_error("A JPEG image was not uploaded! 😡", status_code = 400)

    id = os.urandom(8).hex()
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], id)
    url_path = os.path.join(app.config["UPLOAD_URL_FOLDER"], id)
    full_html_path = os.path.join(app.config["UPLOAD_HTML_FOLDER"], id + ".html")
    html_path = os.path.join(app.config["UPLOAD_REL_HTML_FOLDER"], id + ".html")
    uploaded.stream.seek(0)
    uploaded.save(upload_path)
    
    uploaded_by = request.args.get('name')

    create_page(full_html_path, uploaded_by, url_path)
    insert_db('INSERT INTO "poly-images" ("from", "path") VALUES (?, ?)', args=(uploaded_by, html_path,))

    return json_response({"msg" : "Your JPEG had been uploaded for Poly to review! 🦜", "path" : url_path})

def parse_args():
    parser = argparse.ArgumentParser(description="runs the memedb web api")

    parser.add_argument('-i', '--init', help='initializes the meme db', action="store_true")

    return parser.parse_args()

def main():
    args = parse_args()

    if args.init:
        init_db()
        return
    
    app.run(host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
