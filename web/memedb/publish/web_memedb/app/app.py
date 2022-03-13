from flask import Flask, request, g, escape
from urllib.parse import urlparse
from reviewer import view_meme
from werkzeug.exceptions import HTTPException
import sqlite3, os, json, argparse, glob


app = Flask(__name__)
app.secret_key = os.urandom(64)


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
    CREATE TABLE IF NOT EXISTS "memes" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "name" VARCHAR,
        "url" VARCHAR
    );

    CREATE TABLE IF NOT EXISTS "topsecretmemes" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "name" VARCHAR,
        "url" VARCHAR
    );
    """

    with app.app_context():
        db = get_db()
        db.cursor().executescript(init_script)
        db.commit()
        
    old_name = os.path.join(os.getenv("BASE_MEME_DIR"), "localonly", os.getenv("TOPSECRET_MEME"))
    if not os.path.isfile(old_name):
        return

    secret_meme_name = os.urandom(16).hex() + os.path.splitext(old_name)[1]
    new_name = os.path.join(os.getenv("BASE_MEME_DIR"), "localonly", secret_meme_name)

    os.rename(old_name, new_name)

    secret_url = "/memes/localonly/" + secret_meme_name
    
    insert_db('INSERT INTO topsecretmemes ("name", "url") VALUES ("Mega Dank Secret Meme", ?)', args=(secret_url,))

    for meme_file in glob.glob(os.getenv("BASE_MEME_DIR") + "/*", recursive=False):
        if not os.path.isfile(meme_file):
            continue

        meme_img = meme_file.rsplit("/", 1)[-1]
        meme_name = os.path.splitext(meme_img)[0]
        meme_img = "/memes/" + meme_img

        insert_db('INSERT INTO memes ("name", "url") VALUES (?, ?)', args=(meme_name, meme_img))


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


@app.route("/api/search", methods = ["GET"])
def search_memes():
    search = request.args.get("q", None)
    if not search is None:
        search = "%" + search + "%"
        memes = query_db("SELECT name, url FROM memes WHERE name LIKE ? OR url LIKE ?", args = (search, search))
    else:
        memes = query_db("SELECT name, url FROM memes")

    if not memes:
        return api_error("Could not find any dank memes 😭", status_code = 404)

    return json_response(memes)


@app.route("/api/topsecretmemes/search", methods = ["GET"])
def search_topsecretmemes():
    ip = request.headers.get("X-Real-IP")

    if not ip == "127.0.0.1" or not request.host == "127.0.0.1:4242":
        return api_error("OI! These top secret memes are to be only searched locally within our organisation! 🤬", status_code=403)

    search = request.args.get("q", None)
    passcode = request.args.get("passcode", None)

    if passcode is None:
        return api_error("Missing passcode parameter! 😡", status_code=400)

    if not passcode == "FAKE{THE REAL PASSCODE IS ON THE CHALLENGE INSTANCE}":
        return api_error("Incorrect passcode! 🤬", status_code=401)

    if not search is None:
        search = "%" + search + "%"
        memes = query_db("SELECT name, url FROM topsecretmemes WHERE name LIKE ? OR url LIKE ?", args = (search, search))
    else:
        memes = query_db("SELECT name, url FROM topsecretmemes")
    

    if not memes:
        return api_error("Could not find any dank memes 😭", status_code = 404)

    return json_response(memes)


@app.route("/api/submit", methods = ["POST"])
def submit_meme():
    data = request.get_json()
    if data is None:
        return api_error("You did not send a json document! 😡", status_code=400)

    url = data.get("url", None)

    if not isinstance(url, str):
        return api_error("Missing url for your meme! 😞", status_code=400)

    try:
        validate_url(url)
    except Exception as e:
        return api_error(str(e), status_code=400)

    url = escape(url)

    view_meme(url)

    return json_response("Your meme has been submitted and will be reviewed soon!")

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
