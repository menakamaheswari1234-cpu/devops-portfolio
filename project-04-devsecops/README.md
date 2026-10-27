# Project 4: DevSecOps with SonarQube and Trivy

This project includes a secure DevSecOps workflow.

## Features

- Flask app
- Unit tests
- SonarQube static analysis
- Trivy image scan
- Jenkins pipeline example

## Run locally

```bash
cd project-04-devsecops
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
