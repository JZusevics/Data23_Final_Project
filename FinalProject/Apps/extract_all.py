import boto3
import pandas as pd
from ast import literal_eval
from datetime import datetime
from extract_txt import extract_txt




s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'



def extract_all_talent():
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix='Talent')
    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Talent'
    )

    empty_dicts = {}
    scores_df = []
    csv_df = []
    for page in pages:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj, empty_dicts)
            if 'txt' in obj['Key']:
                scores_df.append(extract_txt(obj['Key']))
            if 'csv' in obj['Key']:
                csv_df.append(extract_csv(obj))
    return extracted_dicts, pd.concat(scores_df), pd.concat(csv_df)


# ensures all names are in title format
x["name"] = x.name.str.title()
# splits name column into first and last name - adds at end of df
x[["first_name", "last_name"]] = x.name.str.split(" ", 1, expand=True)
# pop out name column as no longer needed
x.pop("name")

# x = x["invited_date"].fillna(0)
# # x = x.month.fillna("0")
# x["date_int"] = x.invited_date.astype(int, errors="ignore")
# print(x)
#x["date_int"] = x.invited_date.astype(int, errors="ignore")
x["date_int"] = x.invited_date.astype(str)
x["split"]
x["invitation_date"] = x.invited_date.astype(str) + " " + x.month.str.lower()
#x["invitation_date"] = x.invitation_date.replace({".0": ""}, inplace=True)
x.pop("invited_date")
x.pop("month")
#x.pop("date_int")
print(x)


