from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='static')
    app.config['UPLOAD_FOLDER'] = 'app/uploads/'  # Folder for uploaded files
    app.config['OUTPUT_FOLDER'] = 'app/outputs/'  # Folder for converted files
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Max upload size: 50 MB
    CORS(app)  # Enable cross-origin requests for API
    return app
