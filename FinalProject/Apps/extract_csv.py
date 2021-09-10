import boto3
import pandas as pd


def extract_csv(obj):
    """

    :param obj: the key from the object from s3
    :return: Data Frame from the CSV file
    """
    # get S3 objects
    s3_client = boto3.client('s3')
    bucket_name = 'data23-finalproject-2'
    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=obj['Key']
    )
    df = pd.read_csv(s3_object['Body'])  # convert to dataframe using pandas
    return df  # we need to return dataframe
