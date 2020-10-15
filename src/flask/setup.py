from flask import Flask
from src.flask.endpoint import api

app = Flask(__name__)
api.init_app(app)

#if __name__ == "__main__":
    # hosting API in the following host and port
app.run(host="0.0.0.0", port=5000, debug=True)
