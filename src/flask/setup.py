from flask import Flask
from src.flask.endpoint import api

app = Flask(__name__)
api.init_app(app)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
