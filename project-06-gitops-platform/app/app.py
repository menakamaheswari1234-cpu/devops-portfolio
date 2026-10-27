from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('gitops_app_requests_total', 'Total requests handled by the GitOps demo app')

@app.get('/')
def index():
    REQUEST_COUNT.inc()
    return jsonify({
        "service": "gitops-platform-demo",
        "status": "healthy",
        "environment": "dev",
        "message": "GitOps platform application is running."
    })

@app.get('/health')
def health():
    return jsonify({
        "status": "ok",
        "service": "gitops-platform-demo"
    })

@app.get('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
