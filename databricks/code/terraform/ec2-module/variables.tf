variable "aws_region" { type = string }
variable "instance_count" { type = number }
variable "instance_type" { type = string }
variable "ami_id" { type = string }
variable "key_name" { type = string }
variable "subnet_id" { type = string }
variable "vpc_security_group_ids" { type = list(string) }
variable "tags" { type = map(string) }
variable "public_key_path" { type = string }
variable "iam_instance_profile" { type = string }
