import boto3
import pandas

#Criar um cliente para interagir com AWS

s3_client = boto3.client('s3')

#bucket-name #object-name  #local-file-name
s3_client.download_file('datalake-datashark-edc',
                        'data/func.csv',
                        'funcionario.csv')


df = pandas.read_csv('funcionario.csv')
print(df)


#file_name #object-name  #local-file-name
s3_client.upload_file('awscliv2.zip',
               'datalake-datashark-edc',
                'data/awscliv2.zip' )


