import boto3
import pandas as pd
from ast import literal_eval


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

paginator = s3_client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=bucket_name, Prefix='Talent')


def extract_academy_csv():

    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Academy'
    )

    academy_list = []
    for object in bucket_contents['Contents']:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key=object['Key']
        )
        df = pd.read_csv(s3_object['Body'])
        academy_list.append([object['Key'], df])
    return academy_list

def extract_json():

    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Talent'
    )

    dictionaries = {}
    for page in pages:
        for obj in page['Contents']:
            if '10383.json' in obj['Key']:
                s3_object = s3_client.get_object(
                    Bucket=bucket_name,
                    Key=obj['Key']
                )
                dict = s3_object['Body'].read().decode("utf-8")
                dict = literal_eval(dict)
                name_and_date = dict["name"] + " " + dict["date"]
                dictionaries[name_and_date] = dict
    return dictionaries
