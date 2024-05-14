from flask import Flask, send_from_directory
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize Limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # Directory where the app is located

@app.route('/')
#@limiter.limit("5 per second")
@limiter.limit("120 per hour")
def home():
    return "Hello, this is a Flask app!"

@app.route('/files/<path:filename>')
#@limiter.limit("2 per second") # Limit specifically for this endpoint
@limiter.limit("120 per hour") # Limit specifically for this endpoint
def display_file(filename):
    # This route serves files and allows the browser to handle or display them if possible
    return send_from_directory(DIRECTORY, filename, as_attachment=False)

@app.errorhandler(429)
def ratelimit_handler(e):
    return "Rate limit exceeded. Please try again later.", 429


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8083)

