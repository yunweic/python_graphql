from flask import Flask, jsonify, request
from flask_cors import CORS

# from flask_jwt import JWT
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    jwt_refresh_token_required,
    create_refresh_token,
    get_jwt_identity,
)

import random
import config
import datetime

from user import User

users = [ User(1, 'yunwei', 'password'),
        User(2, 'mimi', 'password') ]

username_tabel = {u.username: u for u in users}

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY

    CORS(app)

    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    jwt = JWTManager(app)

    # Provide a method to create access tokens. The create_access_token()
    # function is used to actually generate the token, and you can return
    # it to the caller however you choose.
    @app.route("/login", methods=["POST"])
    def login():

        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        print("authenticating")

        if username in username_tabel and password == username_tabel[username].password:

            # Use create_access_token() and create_refresh_token() to create our
            # access and refresh tokens
            ret = {
                "access_token": create_access_token(identity=username),
                "refresh_token": create_refresh_token(identity=username),
            }
            return jsonify(ret), 200
        else:
            return jsonify({"msg": "Bad username or password"}), 401

    @app.route("/refresh", methods=["POST"])
    @jwt_refresh_token_required
    def refresh():
        current_user = get_jwt_identity()
        ret = {"access_token": create_access_token(identity=current_user)}
        return jsonify(ret), 200

    return app

if __name__ == "__main__":

    app = create_app()
    app.run(
        host=config.IP_ADDRESS,
        port=config.PORT,
        ssl_context=("./cert/default.crt", "./cert/default.key"),
    )