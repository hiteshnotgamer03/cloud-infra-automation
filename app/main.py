from flask import Flask, jsonify
import time
import os

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def home():
    return jsonify(
        service="cloud-infra-automation",
        message="Cloud-ready Python service is running"
    )

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/metrics")
def metrics():
    uptime = int(time.time() - start_time)
    return jsonify(
        uptime_seconds=uptime,
        environment=os.getenv("ENV", "local")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


