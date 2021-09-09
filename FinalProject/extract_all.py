import boto3
import pandas as pd
from ast import literal_eval
from datetime import datetime



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
    for page in pages:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj, empty_dicts)
            if 'txt' in obj['Key']:
                scores_df.append()
    return extracted_dicts


# extract json files as dictionary of dictionaries
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


def extract_txt(obj,list_df):
    s3_object = s3_client.get_object(
                    Bucket=bucket_name,
                    Key=obj['Key']
                )

    # store txt file as string
    text_file = s3_object['Body'].read().decode('utf-8')
    # separate date, location and candidate info in lists
    lines = text_file.replace(" -", ",").replace("Psychometrics: ", "").replace("Presentation: ", "").splitlines()
    # Store date in date format
    date = datetime.strptime(lines[0], "%A %d %B %Y").date()
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
    list_df.append(df)
    return

x = extract_all_talent()
print(x)