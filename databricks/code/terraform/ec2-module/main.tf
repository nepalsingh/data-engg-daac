provider "aws" {
  region = var.aws_region
}

resource "aws_key_pair" "ec2_key" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

resource "aws_iam_role" "ssm_role" {
  name = "ec2_ssm_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ssm_attach" {
  role       = aws_iam_role.ssm_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_instance_profile" "ssm_profile" {
  name = "ec2_ssm_instance_profile"
  role = aws_iam_role.ssm_role.name
}

module "ec2_instance" {
  source = "./modules/ec2-instance"
  instance_count = var.instance_count
  instance_type  = var.instance_type
  ami_id         = var.ami_id
  key_name       = aws_key_pair.ec2_key.key_name
  subnet_id      = var.subnet_id
  vpc_security_group_ids = var.vpc_security_group_ids
  tags           = var.tags
  iam_instance_profile = aws_iam_instance_profile.ssm_profile.name
}

resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-lock-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
