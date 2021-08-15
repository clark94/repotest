import boto3

#Criar um cliente para interagir com AWS
s3_client = boto3.client('s3')



#file_name #object-name  #local-file-name
s3_client.upload_file('MICRODADOS_ENEM_2019.csv',
               'datalake-lucassantos-285960587752',
                'rawdata/MICRODADOS_ENEM_2019.csv' )
