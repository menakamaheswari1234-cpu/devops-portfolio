from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('demo_requests_total', 'Total requests handled by the app')

@app.get('/')
def index():
    REQUEST_COUNT.inc()
    return jsonify({"service": "monitoring-demo", "status": "healthy"})

@app.get('/health')
def health():
    return jsonify({"status": "ok"})

@app.get('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
