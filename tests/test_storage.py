from flask import Flask
from formidable.storage import FlaskSessionStorage

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"


def test_flask_session_storage():
    with app.test_request_context():
        storage = FlaskSessionStorage()
        storage["csrf_token"] = "test_token"
        assert storage["csrf_token"] == "test_token"
