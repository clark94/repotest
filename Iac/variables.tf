variable "base_bucket_name" {
  default = "datalake-clark-n2-test-tf"

}

variable "ambiente" {
  default = "producao"

}

variable "numero_conta" {
  default = "285960587752"
}

Terraform{
  backend "s3"{
    bucket ="terraformtransformers"
    key="state/terraform.tfstate"
    region ="us-east-2"
  }
}