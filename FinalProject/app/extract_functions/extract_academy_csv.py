from Data23_Final_Project.FinalProject.config_manager import *

# Extracts all CSV data from the ACADEMY bucket and returns them in a LIST
def extract_academy_csv():
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
        # Put the data from the file into a Pandas Data Frame
        df = pd.read_csv(s3_object['Body'])
        academy_list.append([object['Key'], df])
    return academy_list # Return the data from all files in a list

