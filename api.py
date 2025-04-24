from flask import Flask, request, jsonify
from summarize import safe_summarize

app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize_api():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = safe_summarize(text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
