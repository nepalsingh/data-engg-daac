provider "aws" {
  region = "us-east-1"
}

module "secrets_rotation" {
  source = "./modules/secrets-rotation"

  lambda_name = "org-shared-secret-rotation"

  secrets = {
    "mysecretisnottobeshared" = {
      rotation_days = 30
    }

    "another-secret" = {
      rotation_days = 60
    }

    "third-secret" = {
      rotation_days = 15
    }
  }

  tags = {
    Environment = "prod"
    ManagedBy   = "terraform"
  }
}
