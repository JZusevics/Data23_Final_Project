#import packages
import boto3
import pandas as pd
from ast import literal_eval
from datetime import datetime
import json

#connect to s3
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

def extract_json(obj, dictionaries):
    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=obj['Key']
    )

    dict = s3_object['Body'].read().decode("utf-8")
    dict = literal_eval(dict)
    name_and_date = dict["name"] + " " + dict["date"]
    dictionaries[name_and_date] = dict
    return dictionaries

def extract_all_talent():
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix='Talent')
    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Talent'
    )
    empty_dicts = {}
    scores_df = []
    for page in pages:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj, empty_dicts)
        return extracted_dicts

x = extract_all_talent()
with open('data.json', 'w') as fp:
    json.dump(x, fp, sort_keys=True, indent=4)