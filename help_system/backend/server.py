from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

TEMPLATES_DIR = os.path.join(os.getcwd(), "templates")

@app.route("/list", methods=["GET"])
def list_html_files():
    files = [f for f in os.listdir(TEMPLATES_DIR) if f.endswith(".html")]
    return jsonify(files)

@app.route("/upload", methods=["POST"])
def upload_html():
    file = request.files["file"]
    if file.filename.endswith(".html"):
        file.save(os.path.join(TEMPLATES_DIR, file.filename))
        return jsonify({"message": "Archivo subido correctamente"}), 200
    return jsonify({"error": "Solo se permiten archivos .html"}), 400

@app.route("/delete/<filename>", methods=["DELETE"])
def delete_html(filename):
    path = os.path.join(TEMPLATES_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({"message": "Archivo eliminado"}), 200
    return jsonify({"error": "Archivo no encontrado"}), 404

if __name__ == "__main__":
    app.run(port=5000)
