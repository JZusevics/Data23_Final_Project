from Data23_Final_Project.FinalProject.config_manager import *
from Data23_Final_Project.FinalProject.app.extract_functions.extract_academy_csv import *
from Data23_Final_Project.FinalProject.app.extract_functions.extract_talent_txt import *
from Data23_Final_Project.FinalProject.app.extract_functions.extract_talent_json import *
from Data23_Final_Project.FinalProject.app.extract_functions.extract_talent_csv import *


def extract_all():
    """
    :return: list of academy CSV, Json master dictionary, Data Frame of txt data, Data Frame of talent CSV
    """
    # create empty containers
    empty_dicts = {}
    scores_df = []
    csv_df = []
    extracted_dicts = {}

    # call in the academy csv extract function
    academy_csv_df = extract_academy_csv()

    # Extract all data from the Talent bucket
    for page in TALENT_PAGES:
        for obj in page['Contents']:
            if 'json' in obj['Key']:
                extracted_dicts = extract_json(obj['Key'], empty_dicts)
            if 'txt' in obj['Key']:
                scores_df.append(extract_txt(obj['Key']))
            if 'csv' in obj['Key']:
                csv_df.append(extract_csv(obj['Key']))
    return academy_csv_df, extracted_dicts, pd.concat(scores_df), pd.concat(csv_df)
