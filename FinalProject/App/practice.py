import io
import json
import pandas as pd
import boto3
import pprint as pp

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

bucket_contents = s3_client.list_objects_v2(
    Bucket=bucket_name,
    Prefix='Academy'
)

# pp.pprint(bucket_contents)
# for content in bucket_contents['Contents']:
#     pp.pprint(content)

academy_list = []
for object in bucket_contents['Contents']:
    #print(object)
    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=object['Key']
    )
    df = pd.read_csv(s3_object['Body'])
    academy_list.append([object['Key'], df])
    #print(df.first())
print(len(academy_list))
print(academy_list[0][0])
pp.pprint(academy_list[0][1])



