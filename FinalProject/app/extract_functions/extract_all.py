from FinalProject.config_manager import *
from extract_talent_txt import *
from extract_academy_csv import *
from extract_talent_csv import *
from extract_talent_json import *


def extract_all():
    """
    :return: list of academy CSV, Json master dictionary, Data Frame of txt data, Data Frame of talent CSV
    """
    #create empty containers
    empty_dicts = {}
    scores_df = []
    csv_df = []
    academy_csv_list =[]

    # call in all the academy csv
    academy_csv_list = extract_academy_csv()

    # Extract all data from the Talent bucket
    for page in TALENT_PAGES:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj, empty_dicts)
            if 'txt' in obj['Key']:
                scores_df.append(extract_txt(obj['Key']))
            if 'csv' in obj['Key']:
                csv_df.append(extract_csv(obj))
    return academy_csv_list, extracted_dicts, pd.concat(scores_df), pd.concat(csv_df)