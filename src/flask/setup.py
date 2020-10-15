import os
from flask import Flask
from src.flask.endpoint import api

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
api.init_app(app)

if __name__ == "__main__":
    # hosting API in the following host and port
    context = ('local.crt', 'local.key')
    app.run(host="https://rafiquicf.herokuapp.com", port=os.environ.get("PORT", 5000), debug=True)
