from flask import Flask, send_from_directory, request
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize Limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["14400 per day", "60 per hour"]
)

DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # Directory where the app is located

# Apply rate limit to all requests
@app.before_request
#@limiter.limit("5 per second")
@limiter.limit("60 per minute")
def before_request_func():
    # This function will run before every request, applying the rate limit
    pass

@app.route('/')
def home():
    return "Hello, this is a Flask app!"

@app.route('/files/<path:filename>')
def display_file(filename):
    # This route serves files and allows the browser to handle or display them if possible
    return send_from_directory(DIRECTORY, filename, as_attachment=False)

@app.errorhandler(404)
def page_not_found(e):
    return "This page does not exist.", 404

@app.errorhandler(429)
def ratelimit_handler(e):
    return "Rate limit exceeded. Please try again later.", 429

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8083)
    app.run(host='0.0.0.0', port=80)

