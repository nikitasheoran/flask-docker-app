<<<<<<< HEAD
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return os.getenv("APP_MESSAGE")

@app.route("/health")
def health():
    return os.getenv("APP_HEALTH")

if __name__ == "__main__":
=======
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return os.getenv("APP_MESSAGE")

@app.route("/health")
def health():
    return os.getenv("APP_HEALTH")

if __name__ == "__main__":
>>>>>>> dba98066c0f78d24bcbcf7121335cee434aca3ad
    app.run(host="0.0.0.0", port=5000)