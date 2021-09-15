from FinalProject.config_manager import *
from FinalProject.app.extract.extract_academy_csv import *
from FinalProject.app.extract.extract_talent_txt import *
from FinalProject.app.extract.extract_talent_json import *
from FinalProject.app.extract.extract_talent_csv import *


def extract_all(extracted_list: list):
    """
    :param extracted_list: List of files that have been extracted. This is used to ensure only new files are extracted
    :return: list of academy CSV, Json master dictionary, Data Frame of txt data, Data Frame of talent CSV
    """
    # create empty containers
    empty_dicts = {}
    scores_df = []
    csv_df = []
    extracted_dicts = {}

    # call in the academy csv extract function
    academy_csv_df = extract_academy_csv(extracted_list)

    # Extract all data from the Talent bucket

    for page in TALENT_PAGES:
        for obj in page['Contents']:
            if obj['Key'] not in extracted_list:
                if 'json' in obj['Key']:
                    extracted_dicts = extract_json(obj['Key'], empty_dicts)
                    extracted_list.append(obj['Key'])
                elif 'txt' in obj['Key']:
                    scores_df.append(extract_txt(obj['Key']))
                    extracted_list.append(obj['Key'])
                elif 'csv' in obj['Key']:
                    csv_df.append(extract_csv(obj['Key']))
                    extracted_list.append(obj['Key'])
    return academy_csv_df, extracted_dicts, pd.concat(scores_df), pd.concat(csv_df)