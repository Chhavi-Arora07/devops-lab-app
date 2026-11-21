terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

variable "instance_count" {
  description = "Number of web servers"
  type        = number
  default     = 2
}

resource "docker_image" "nginx" {
  name = "nginx:alpine"
}

resource "docker_container" "web" {
  count = var.instance_count
  name  = "tf-web-${count.index + 1}"
  image = docker_image.nginx.image_id

  ports {
    internal = 80
    external = 8081 + count.index
  }
}

output "web_urls" {
  value = [for i in range(var.instance_count) : "http://localhost:${8081 + i}"]
}