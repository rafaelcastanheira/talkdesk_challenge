from flask import Flask
from src.flask.endpoint import api

app = Flask(__name__)
api.init_app(app)

app.run(host="localhost", port=5000, debug=True)
