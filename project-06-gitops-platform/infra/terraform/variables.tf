variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "gitops-demo"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "gitops-demo-cluster"
}
