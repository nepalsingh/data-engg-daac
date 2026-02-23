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
