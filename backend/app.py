from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import parse_resume

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    parsed_data = parse_resume(file)
    return jsonify(parsed_data)

if __name__=="__main__":
    app.run(debug=True)