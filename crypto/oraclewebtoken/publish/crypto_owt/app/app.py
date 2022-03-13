from flask import Flask, request
from itsdangerous import exc
from werkzeug.exceptions import HTTPException
import os, logging, json, binascii

import owt

app = Flask(__name__)
app.secret_key = binascii.unhexlify(os.getenv("SECRET_KEY"))

app.config['FLAG'] = os.getenv("FLAG")
logging.basicConfig(level=logging.INFO)

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

@app.errorhandler(Exception)
def endpoint_not_found(e):
    if isinstance(e, HTTPException):
        e: HTTPException = e
        return api_error(e.description, e.code)
    return api_error("You broke something! ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾", 500)

@app.route('/api/token/create', methods=["GET"])
def create_token():
    data = {
        "flag" : app.config["FLAG"]
    }
    try:
        return json_response({"token":owt.create_token(data, app.config["SECRET_KEY"])})
    except Exception as e:
        return api_error("Something went wrong trying to create a OWT token for you :(.")

@app.route('/api/token/verify', methods=["POST"])
def verify_token():
    data = request.get_json()
    token = data.get("token", None)
    if not isinstance(token, str):
        return api_error("You did not send a token!", status_code=400)

    try:
        owt.decrypt_token(token, app.config["SECRET_KEY"])
        return json_response("Token is a valid OWT token!")
    except owt.OWTException as e:
        return api_error("Verification Failed: {}".format(e), status_code=400)

def main():
    app.run(host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
