import io
import json
import pandas as pd
import boto3
import pprint as pp
from datetime import datetime


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

def extract_academy_txt():

    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Talent'
    )
    scores_df = []
    for page in pages:
        for obj in page['Contents']:
            if 'txt' in obj['Key']:
                s3_object = s3_client.get_object(
                    Bucket=bucket_name,
                    Key=obj['Key']
                )
            # store txt file as string
            text_file = s3_object['Body'].read().decode('utf-8')
            # separate date, location and candidate info in lists
            lines = text_file.replace(" -", ",").replace("Psychometrics: ","").replace("Presentation: ","").splitlines()
            # Store date in date format
            date = datetime.strptime(lines[0],"%A %d %B %Y").date()
            location = lines[1]
            # from 3rd line data has name, psychometrics and presentation scores
            candidate_data = lines[3:-1]

            # create variables for separating
            names = []
            psychometrics = []
            presentation = []


            for item in candidate_data:
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
                score_list = item.split("/")
                score_list = round((int(score_list[0]) / int(score_list[1]) * 100), 2)
                presentation_scores.append(score_list)

            df = pd.DataFrame(names, columns=["Names"])
            df.insert(1, "Psychometrics Score", psychometrics_score, True)
            df.insert(2, "Presentation Score", presentation_scores, True)
            df.insert(3, "Date", date, True)
            df.insert(4, "Location", location, True)
            scores_df.append(df)

    return scores_df
print(extract_academy_txt())