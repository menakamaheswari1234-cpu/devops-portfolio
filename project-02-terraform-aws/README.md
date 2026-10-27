# Project 2: Terraform AWS Infrastructure Automation

This project provisions a basic AWS network and compute environment using Terraform.

## Features

- VPC
- Public subnet
- Internet gateway
- Security group
- EC2 instance
- S3 bucket

## Usage

```bash
cd project-02-terraform-aws
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply
```

## Destroy

```bash
terraform destroy
```
