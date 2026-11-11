from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "NEXUS",
        "message": "Welcome to NEXUS DevOps Platform!",
        "status": "Running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "NEXUS"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)