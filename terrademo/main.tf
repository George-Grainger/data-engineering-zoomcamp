terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.16.0"
    }
  }
}

provider "google" {
  project = "pivotal-purpose-414614"
  region  = "europe-west2"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "pivotal-purpose-414614-terra-bucket"
  location      = "EUROPE-WEST2"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}