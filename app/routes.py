import os
from flask import Blueprint, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from app.converters import convert_pdf
from app.utils import allowed_file

# Create a Flask Blueprint for routing
routes = Blueprint('routes', __name__)

# Route: Render the main conversion page
@routes.route('/')
def index():
    """
    Serves the index.html.
    """
    return render_template('index.html')
@routes.route('/convert')
def convert():
    """
    Serves the convert.html page where file upload and conversion happen.
    """
    return render_template('convert.html')  # Serve the single conversion page

# Route: Handle file upload and conversion
@routes.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles file uploads, validates the file type, and triggers the conversion process.
    """
    # Check if the request has a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    conversion_type = request.form.get('conversion_type')  # Get the conversion type

    # Validate the uploaded file
    if file and allowed_file(file.filename):
        # Save the uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join('app/uploads/', filename)
        file.save(input_path)

        # Perform the conversion
        output_path = convert_pdf(input_path, conversion_type)
        if output_path:
            # Conversion successful; return download link
            return jsonify({'output': f'/download/{os.path.basename(output_path)}'}), 200
        else:
            return jsonify({'error': 'Conversion failed'}), 500
    else:
        # Invalid file type or no file uploaded
        return jsonify({'error': 'Invalid file type'}), 400

# Route: Download converted file
@routes.route('/download/<filename>')
def download_file(filename):
    """
    Serves the converted file for download.
    """
    return send_from_directory('app/outputs/', filename, as_attachment=True)

# Route: Additional navigation pages (if needed)
@routes.route('/about')
def about():
    """
    Serves the about.html page.
    """
    return render_template('about.html')

@routes.route('/changelog')
def changelog():
    """
    Serves the changelog.html page.
    """
    return render_template('changelog.html')

@routes.route('/faq')
def faq():
    """
    Serves the faq.html page.
    """
    return render_template('faq.html')
