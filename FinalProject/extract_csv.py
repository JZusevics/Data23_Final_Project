import boto3
import pandas as pd

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data23-finalproject-2'

# this function extracts all CSV files from data23-finalproject-2/Academy and stores them into a list
def extract_academy_csv():
      """
    
    :return: dataframe of all academy CSV files with course names and dates
    """
    
    bucket_contents = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix='Academy'  # specify the Academy prefix within the data23-finalproject-2 bucket
    )

    academy_list = []  # empty list to store all the files
    for object in bucket_contents['Contents']:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key=object['Key']
        )
        # convert data into a dataframe
        df = pd.read_csv(s3_object['Body'])
        # from the csv file title, we extract course dates and names
        # add these as a column in the dataframe
        df.insert(2, 'course_start_date', object['Key'].split(".")[0].split("_")[2])
        df.insert(3, 'course_name', object['Key'].split("/")[1].split(".")[0].split("_")[0])
        df.insert(4, 'course_number', object['Key'].split("/")[1].split(".")[0].split("_")[1])
        # store dataframes in a list
        academy_list.append(df)

    return pd.concat(academy_list)  # outputs the dataframes in concatenated format
