from flask import Flask, request, jsonify, redirect
from models import shorten_url, get_original_url

app = Flask(__name__)

@app.route("/shorten", methods=["POST"])
def shorten():
    """Receives a long URL and returns a short URL."""
    data = request.json
    if "url" not in data:
        return jsonify({"error": "URL is required"}), 400
    
    short_id = shorten_url(data["url"])
    return jsonify({"short_url": f"http://127.0.0.1:5050/{short_id}"})

@app.route("/<short_id>")
def redirect_url(short_id):
    """Redirects short URL to the original long URL."""
    original_url = get_original_url(short_id)
    if original_url:
        return redirect(original_url)
    
    return jsonify({"error": "Short URL not found"}), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
