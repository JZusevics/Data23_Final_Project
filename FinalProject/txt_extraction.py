import io
import json
import pandas as pd
import boto3
import pprint as pp
from datetime import datetime


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

bucket = s3_resource.Bucket(bucket_name)
objects = bucket.objects
contents = objects.all()
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Talent/Sparta Day 16 October 2019.txt'
)
textfile = s3_object['Body'].read().decode('utf-8')
lines = textfile.replace(" -", ",").replace("Psychometrics: ","").replace("Presentation: ","").splitlines()
# print(lines[0])
date = datetime.strptime(lines[0],"%A %d %B %Y").date()
location = lines[1]
data = lines[3:-1]
names = []
psychometrics = []
presentation = []

for item in data:
    sparta_list = item.split(",")
    names.append(sparta_list[0].lower().title())
    psychometrics.append(sparta_list[1].strip())
    presentation.append(sparta_list[2].strip())

psychometrics_score = []
for item in psychometrics:
    score_list = item.split("/")
    score_list = round((int(score_list[0]) / int(score_list[1]) * 100), 2)
    psychometrics_score.append(score_list)

presentation_scores = []
for item in presentation:
    score_list= item.split("/")
    score_list = round((int(score_list[0])/int(score_list[1])*100),2)
    presentation_scores.append(score_list)

df = pd.DataFrame(names, columns = ["Names"])
df.insert(1, "Psychometrics Score",psychometrics_score, True)
df.insert(2, "Presentation Score",presentation_scores, True)
df.insert(3, "Date",date, True)
df.insert(4, "Location",location, True)
print(df)