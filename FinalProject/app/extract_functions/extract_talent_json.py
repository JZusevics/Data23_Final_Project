from Data23_Final_Project.FinalProject.config_manager import *

# Extracts all the JSON data from the specified object and returns it in a dictionary
def extract_json(key, dictionaries):
    """

    :param key: Selects s3 key to extract
    :param dictionaries: Initially empty dictionary to have json files appended to
    :return: dictionary of json names and files {"name_and_date": "json"}
    """
    # get s3 object
    s3_object = S3_CLIENT.get_object(
        Bucket=S3_BUCKET,
        Key=key
    )
    # Read json contents in appropriate format
    dict = s3_object['Body'].read().decode("utf-8")
    dict = literal_eval(dict)
    # Extract and assign name + date as key for each json file
    name_and_date = dict["name"] + " " + dict["date"]
    dictionaries[name_and_date] = dict
    return dictionaries ## return dictionary

    # Extracts all JSON data from the TALENT bucket and returns them in a dictionary with a name + date value as key
def extract_just_json(bucket_name):
    """
    This file is the final function to allow for the exctraction of just json files from the s3 bucket
    it will not be run in main
    :param bucket_name: The location of the s3 bucket
    :return: A dictionary of json files and names for conversion into a json file
    """

    empty_dicts = {}
    for page in TALENT_PAGES:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj['Key'], empty_dicts)
        return extracted_dicts


## For testing and data exploration
if __name__ == '__main__':
    x = extract_just_json(S3_BUCKET)
    # saves json onto local machine
    with open('talent_json_data', 'w') as fp:
        json.dump(x, fp, sort_keys=True, indent=4)