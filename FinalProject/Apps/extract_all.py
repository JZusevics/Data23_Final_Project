from extract_txt import *
from extract_json import *
from extract_csv import *


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'


def extract_all_talent():
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix='Talent')

    empty_dicts = {}
    scores_df = []
    csv_df = []
    for page in pages:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj['Key'], empty_dicts)
            if 'txt' in obj['Key']:
                scores_df.append(extract_txt(obj['Key']))
            if 'csv' in obj['Key']:
                csv_df.append(extract_csv(obj['Key']))
    return extracted_dicts, pd.concat(scores_df), pd.concat(csv_df)

