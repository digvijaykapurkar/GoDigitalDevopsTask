# Terraform - .tf file for automate the AWS Cloud Infrastructure

provider "aws" {
    access_key = "AKIATCKATAF2WQNNFK6N"
    secret_key = "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"
    region = "ap-south-1"
}
resource "aws_db_instance" "db" {
  allocated_storage    = 10
  db_name              = "db7385"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "taskdb"
  password             = "taskdb123*"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
}

resource "aws_s3_bucket" "b" {
  bucket = "task-bucket7385"
}

resource "aws_ecr_repository" "ecr-repo" {
  name                 = "ecrrepo"
  image_tag_mutability = "MUTABLE"
}
