from flask import Flask, request
import tempfile
import os
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')

def image_to_text(file_path):
    result = ocr.ocr(file_path, cls=False, det=False)
    return {'data': result[0][0][0]}, 200

app = Flask(__name__)

@app.route("/health")
def health():
    return "HEALTHY"

@app.route('/process', methods=['POST'])
def process():
    # Check if the request contains a file
    if 'file' not in request.files:
        return 'No file found', 400

    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return 'No file selected', 400

    # Save the file to a temporary location
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, file.filename)
    file.save(temp_file_path)

    return image_to_text(temp_file_path)
