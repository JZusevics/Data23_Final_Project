import boto3
import pandas as pd


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

# this function extracts all CSV files from data23-finalproject-2/Academy and stores them into a list
def extract_academy_csv():

    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Academy'  # specify the Academy prefix within the data23-finalproject-2 bucket
    )

    academy_list = []  # empty list to store all the files
    for object in bucket_contents['Contents']:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key=object['Key']
        )
        df = pd.read_csv(s3_object['Body'])
        academy_list.append([object['Key'], df])
    return academy_list
