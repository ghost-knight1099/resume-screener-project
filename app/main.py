from flask import Flask, request, jsonify
from flask_cors import CORS
from app.parser import parse_resume  # your function

app = Flask(__name__)
CORS(app)  # 🔥 Enables Cross-Origin access from frontend

@app.route("/")
def index():
    return "Hello World"

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    result = parse_resume(file)
    return jsonify(result)

if __name__ == '__main__':
    print("🔥 Flask app is starting on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
