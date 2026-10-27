# GitOps Multi-Environment Platform on AWS

This project is a production-style portfolio project that brings together infrastructure automation, Kubernetes deployment, GitOps workflows, security checks, and observability.

## Why this project is unique

This is a platform project rather than a single app demo. It demonstrates how a modern DevOps team would manage multiple environments with automation and operational maturity.

### Included capabilities

- Terraform for AWS infrastructure provisioning
- EKS cluster setup and Kubernetes workloads
- GitHub Actions CI pipeline
- Container image build and security scanning
- ArgoCD-style GitOps deployment workflow
- Prometheus and Grafana monitoring
- Multi-environment patterns for dev / staging / prod
- App health checks and rollback-friendly deployment design

## Architecture

```text
Developer -> GitHub -> GitHub Actions -> Docker Build -> Trivy Scan -> Terraform/EKS -> ArgoCD -> Kubernetes
                                         |
                                         +-> SonarQube quality gate
                                         
Application -> Prometheus -> Grafana
```

## Project structure

```text
project-06-gitops-platform/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── infra/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── providers.tf
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── helm/
│   └── app/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── monitoring/
│   ├── prometheus.yaml
│   └── grafana-dashboard.json
├── .github/workflows/
│   └── ci.yml
├── scripts/
│   └── deploy.sh
├── tests/
│   └── test_app.py
├── README.md
├── .gitignore
└── .env.example
```

## Prerequisites

To run the project locally, install:

- Python 3.11+
- Docker & Docker Compose
- Terraform 1.5+
- kubectl
- Helm
- Minikube or kind (optional for local Kubernetes)

## Local app run

```bash
cd project-06-gitops-platform/app
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app.py
```

Open:

- http://localhost:5000/
- http://localhost:5000/health
- http://localhost:5000/metrics

## Docker run

```bash
cd project-06-gitops-platform/app
docker build -t gitops-demo:local .
docker run -p 5000:5000 gitops-demo:local
```

## Helm deployment example

```bash
cd project-06-gitops-platform/helm/app
helm install gitops-demo .
helm list
```

## Terraform example

```bash
cd project-06-gitops-platform/infra/terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply
```

## GitHub Actions CI

The workflow included under `.github/workflows/ci.yml` performs:

- checkout
- Python dependency install
- test execution
- Docker image build
- Trivy vulnerability scan

## Monitoring

Prometheus scrape config and Grafana dashboard example are included under `monitoring/`.

## Security practices

- No real credentials or secrets are committed
- Use `.env.example` or GitHub secrets for real deployments
- Restrict AWS ingress and IAM rights with least privilege
- Prefer private networking and secure Kubernetes access in production

## Troubleshooting

- App not reachable: ensure the port is 5000 and the container is running.
- Terraform errors: verify AWS credentials and region configuration.
- Kubernetes issues: ensure `kubectl` is connected to a cluster.
- Monitoring not scraping: confirm service names and port mappings in Prometheus config.

## Cleanup

```bash
helm uninstall gitops-demo
terraform destroy
```

## Portfolio value

This project demonstrates that you can design and operate a modern platform using:

- GitOps principles
- Cloud automation
- Container orchestration
- Security checks
- Monitoring and reliability practices

That is highly relevant for DevOps Engineer, AWS Cloud Engineer, and SRE interview narratives.
