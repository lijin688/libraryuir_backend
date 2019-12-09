import sys
from flask import Flask, request
from flask_cors import *


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    # server端支持跨域访问
    CORS(app, supports_credentials=True)

    from libraryuir.web.book_view import views as book_view
    app.register_blueprint(book_view)
    return app