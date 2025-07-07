variable "instance_count" { type = number }
variable "instance_type" { type = string }
variable "ami_id" { type = string }
variable "key_name" { type = string }
variable "subnet_id" { type = string }
variable "vpc_security_group_ids" { type = list(string) }
variable "tags" { type = map(string) }
variable "iam_instance_profile" { type = string }

resource "aws_instance" "this" {
  count         = var.instance_count
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = var.subnet_id
  vpc_security_group_ids = var.vpc_security_group_ids
  iam_instance_profile   = var.iam_instance_profile != "" ? var.iam_instance_profile : null

  tags = var.tags
}

output "instance_ids" {
  value = aws_instance.this[*].id
}
