#import packages
import boto3
import pandas as pd
from ast import literal_eval
from datetime import datetime
import json


#connect to s3
s3_client = boto3.client('s3')
bucket_name = 'data23-finalproject-2'

def extract_json(key, dictionaries):
    """
    :param key: Selects s3 key to extract
    :param dictionaries: Initially empty dictionary to have json files appended to
    :return: dictionary of json names and files {"name_and_date": "json"}
    """
    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=key
    )

    dict = s3_object['Body'].read().decode("utf-8")
    dict = literal_eval(dict)
    name_and_date = dict["name"] + " " + dict["date"]
    dictionaries[name_and_date] = dict
    return dictionaries


def extract_just_json(bucket_name):
    """
    This file is the final function to allow for the exctraction of just json files from the s3 bucket
    it will not be run in main
    :param bucket_name: The location of the s3 bucket
    :return: A dictionary of json files and names for conversion into a json file
    """
    empty_dicts = {}
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix='Talent')
    for page in pages:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj['Key'], empty_dicts)
    return extracted_dicts

x = extract_just_json(bucket_name)

# saves json onto local machine
with open('data.json', 'w') as fp:
    json.dump(x, fp, sort_keys=True, indent=4)