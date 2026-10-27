# Project 5: Kubernetes Monitoring with Prometheus and Grafana

This project demonstrates Kubernetes monitoring with Prometheus and Grafana.

## Features

- Flask app exposing metrics
- Prometheus scrape config
- Grafana dashboard example
- Kubernetes deployment example

## Run locally

```bash
cd project-05-kubernetes-monitoring
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app.py
```
