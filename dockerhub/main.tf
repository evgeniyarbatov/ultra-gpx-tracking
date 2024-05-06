terraform {
  required_version = ">=1"
}

variable "image_name" {
  type = string
}

variable "source_path" {
  type = string
}

variable "base_repository_url" {
  default = "evgenyarbatov"
}

variable "tag" {
  default = "latest"
}

resource "null_resource" "push" {
  provisioner "local-exec" {
    command     = "${path.module}/push.sh ${var.source_path} ${var.base_repository_url}/${var.image_name} ${var.tag}"
    interpreter = ["bash", "-c"]
  }
  triggers = {
    always_run = "${timestamp()}"
  }
}