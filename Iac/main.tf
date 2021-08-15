resource "aws_s3_bucket" "datalake" {

  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  acl    = "private"
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"

      }

    }
  }

  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }


}

resource "aws_s3_bucket_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/jobspark/job_spark_to_tf.py"
  source = "../job_spark.py"
  acl    = "private"

  # The filemd5() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the md5() function and the file() function:
  # etag = "${md5(file("path/to/file"))}"
  etag = filemd5("../job_spark.py")
}



provider "aws" {
  region = "us-east-2"

}