variable "creds-path" {
  description = "Path to file containing credentials"
  default = "./keys/creds.json"
}

variable "project" {
  description = "Project"
  default = "pivotal-purpose-414614"
}

variable "region" {
  description = "Project region"
  default     = "europe-west2"
}


variable "location" {
  description = "Project location"
  default     = "EUROPE-WEST2"
}

variable "bq_dataset_name" {
  description = "My BigQuert Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Bucket Name"
  default     = "pivotal-purpose-414614-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

