# Terraform Code for AWS Lambda Rotation
-- IAM Role

``` IAM Role
resource "aws_iam_role" "rotation_role" {
  name = "${var.lambda_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })

  tags = var.tags
}

```

-- varables.tf

``` variables.tf
variable "secrets" {
  description = "Map of secret names and rotation settings"
  type = map(object({
    rotation_days = number
  }))
}

variable "lambda_name" {
  description = "Name of shared rotation lambda"
  type        = string
  default     = "shared-secret-rotation"
}

variable "lambda_timeout" {
  type    = number
  default = 30
}

variable "tags" {
  type    = map(string)
  default = {}
}
```

-- main.tf

``` main.tf
data "aws_secretsmanager_secret" "targets" {
  for_each = var.secrets
  name     = each.key
}
```

``` IAM Policy (Scoped to Provided Secrets)

resource "aws_iam_role_policy" "rotation_policy" {
  name = "${var.lambda_name}-policy"
  role = aws_iam_role.rotation_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:PutSecretValue",
          "secretsmanager:DescribeSecret",
          "secretsmanager:UpdateSecretVersionStage"
        ]
        Resource = [
          for s in data.aws_secretsmanager_secret.targets :
          s.arn
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}
```

--- shared lambda function

``` shared lambda

resource "aws_lambda_function" "rotation" {
  function_name = var.lambda_name
  role          = aws_iam_role.rotation_role.arn
  handler       = "rotation.lambda_handler"
  runtime       = "python3.11"
  timeout       = var.lambda_timeout

  filename         = "${path.module}/lambda/rotation.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda/rotation.zip")

  tags = var.tags
}
```

-- Allow Invocation (Per Secret)

``` Allow Invocation (Per Secret)
resource "aws_lambda_permission" "allow_secrets_manager" {
  for_each = var.secrets

  statement_id  = "AllowSecretsManagerInvoke-${each.key}"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.rotation.function_name
  principal     = "secretsmanager.amazonaws.com"
  source_arn    = data.aws_secretsmanager_secret.targets[each.key].arn
}
```

-- Enable Rotation Per Secret
```
resource "aws_secretsmanager_secret_rotation" "rotation" {
  for_each = var.secrets

  secret_id           = data.aws_secretsmanager_secret.targets[each.key].id
  rotation_lambda_arn = aws_lambda_function.rotation.arn

  rotation_rules {
    automatically_after_days = each.value.rotation_days
  }

  depends_on = [
    aws_lambda_permission.allow_secrets_manager
  ]
}
```
-- outputs.tf

``` outputs.tf
output "lambda_name" {
  value = aws_lambda_function.rotation.function_name
}

output "rotated_secrets" {
  value = keys(var.secrets)
}
```

-- zip rotation.zip rotation.py

``` zip

zip rotation.zip rotation.py
```

```
resource "aws_iam_role" "rotation_role" {
  name = "${var.secret_name}-rotation-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

```
