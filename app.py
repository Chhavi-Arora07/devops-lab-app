import os
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Feature flag, controlled from outside the code
FEATURE_NEW_GREETING = os.getenv("FEATURE_NEW_GREETING", "false").lower() == "true"

@app.route("/")
def home():
    if FEATURE_NEW_GREETING:
        return "<h1 id='greeting'>Hello from DevOps Lab! (new feature ON)</h1>"
    return "<h1 id='greeting'>Hello from DevOps Lab!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)