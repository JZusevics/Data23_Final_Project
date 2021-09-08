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

# pp.pprint(bucket_contents)
# for content in bucket_contents['Contents']:
#     pp.pprint(content)

applicant_csv_list = []
json_list = []
txt_list = []
for page in pages:
    for obj in page['Contents']:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key=obj['Key']
        )
        if 'csv' in obj['Key']:
            df = pd.read_csv(s3_object['Body'])
            applicant_csv_list.append(df)
        elif 'json' in obj['Key']:
            #print(s3_object)
            dict = s3_object['Body'].read()
            json_list.append(dict)
        elif 'txt' in obj['Key']:
            df = pd.read_csv(s3_object['Body'])
            txt_list.append(df)
json_list1 = json_list

    #print(df.first())
#print(len(bucket_contents['Contents']))
print(len(applicant_csv_list))
print(len(json_list))
print(json_list1[0])
print(len(txt_list))
# pp.pprint(applicant_csv_list[0][1])
