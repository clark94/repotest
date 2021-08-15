# Comentário para modificar o arquivo .py 2
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Ler os dados do enem 2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-lucassantos-285960587752/rawdata/")
)


(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-lucassantos-285960587752/staging/")
    
)