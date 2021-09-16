from FinalProject.config_manager import *


def extract_csv(key):
    """
    :param obj: the key from the object from s3
    :return: Data Frame from the CSV file
    """
    # get S3 objects
    s3_object = S3_CLIENT.get_object(
        Bucket=S3_BUCKET,
        Key=key
    )
    df = pd.read_csv(s3_object['Body'])  # convert to dataframe using pandas
    return df  # we need to return dataframe
