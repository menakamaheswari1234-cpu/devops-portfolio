# Project 1: Jenkins CI/CD with Docker and Kubernetes

This project demonstrates an end-to-end CI/CD pipeline using Jenkins, Docker, and Kubernetes.

## Features

- Python Flask app
- Dockerized build
- Jenkins pipeline
- Kubernetes deployment manifests
- Health checks and rollback-friendly deployment structure

## Run locally

```bash
cd project-01-jenkins-cicd
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app.py
```

## Docker

```bash
docker build -t jenkins-cicd-demo .
docker run -p 5000:5000 jenkins-cicd-demo
```

## Kubernetes

```bash
kubectl apply -f k8s/
```

## Notes

Use placeholder credentials and avoid committing secrets.
