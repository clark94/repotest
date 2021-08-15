provider "aws" {
  region = "us-east-2"

}

terraform{
  backend "s3"{
    bucket ="terraformtransformers"
    key="state/terraform.tfstate"
    region ="us-east-2"
  }
}
