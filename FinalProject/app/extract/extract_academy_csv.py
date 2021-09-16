from FinalProject.config_manager import *


# Extracts all CSV data from the ACADEMY bucket and returns them in a pandas dataframe
def extract_academy_csv(extracted_keys: list):
    """
    :return: List of Data Frames
    """
    academy_list = []  # empty list to store all the files
    # For each file in the bucket
    for object in BUCKET_CONTENTS_ACADEMY['Contents']:
        # Get object info
        s3_object = S3_CLIENT.get_object(
            Bucket=S3_BUCKET,
            Key=object['Key']
        )
        if object['Key'] not in extracted_keys:
            # convert data into a dataframe
            df = pd.read_csv(s3_object['Body'])
            # from the csv file title, we extract course dates and names
            # add these as a column in the dataframe
            df.insert(2, 'course_start_date', object['Key'].split(".")[0].split("_")[2])
            df.insert(3, 'course_name', object['Key'].split("/")[1].split(".")[0].split("_")[0])
            df.insert(4, 'course_number', object['Key'].split("/")[1].split(".")[0].split("_")[1])
            # store dataframes in a list
            academy_list.append(df)
            extracted_keys.append(object['Key'])
    return pd.concat(academy_list)  # outputs the dataframes in concatenated format
