from flask import Flask, send_from_directory
import os

app = Flask(__name__)
DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # Directory where the app is located

@app.route('/')
def home():
    return "Hello, this is a Flask app!"

@app.route('/files/<path:filename>')
def display_file(filename):
    # This route serves files and allows the browser to handle or display them if possible
    return send_from_directory(DIRECTORY, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8083)

