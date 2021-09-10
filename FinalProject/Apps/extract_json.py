#import packages
import boto3
from ast import literal_eval

#connect to s3
s3_client = boto3.client('s3')
bucket_name = 'data23-finalproject-2'

def extract_json(key, dictionaries):
    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=key
    )

    dict = s3_object['Body'].read().decode("utf-8")
    dict = literal_eval(dict)
    name_and_date = dict["name"] + " " + dict["date"]
    dictionaries[name_and_date] = dict
    return dictionaries