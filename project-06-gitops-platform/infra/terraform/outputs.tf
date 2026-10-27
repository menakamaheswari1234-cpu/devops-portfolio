output "vpc_id" {
  description = "VPC id"
  value       = aws_vpc.main.id
}

output "cluster_name" {
  description = "Target EKS cluster name"
  value       = var.cluster_name
}
