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
