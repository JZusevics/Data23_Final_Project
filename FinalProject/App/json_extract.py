import io
import json
import pandas as pd
import boto3
import pprint as pp

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

paginator = s3_client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=bucket_name, Prefix='Talent')

bucket_contents = s3_client.list_objects_v2(
    Bucket=bucket_name,
    Prefix='Talent'
)


