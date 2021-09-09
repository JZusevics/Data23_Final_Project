import io
import json
import pandas as pd
import boto3
import pprint as pp
from ast import literal_eval

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key="Talent/13383.json"
)

dictionaries = {}

df = s3_object["Body"].read().decode("utf-8")

dict = literal_eval(df)
#print(dict)
#print(type(dict))
name_and_date = dict["name"] + " " + dict["date"]
#print(name_and_date)


dictionaries[name_and_date] = dict
print(dictionaries)