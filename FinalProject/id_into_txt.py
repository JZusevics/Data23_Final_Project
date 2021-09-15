import pandas as pd
import numpy as np

def candidate_id_into_txt(csv: pd.DataFrame, txt: pd.DataFrame):
    """

    :param csv: csv dataframe generated from the extraction stage of the ETL pipeline
    :param txt: txt dataframe generated from the extraction stage of the ETL pipeline
    :return: txt dataframe with candidate_id columns that match the csv candidate_id column
    """
    txt['applicant_day_date'] = txt['date']  # change name in text table so you have uniform columns names
    # use a join to get the correct ids for each candidate
    new = pd.merge(txt, csv, on=['full_name', 'applicant_day_date'], how='outer', indicator=True)
    # add this into the txt dataframe
    txt['candidate_id'] = new['candidate_id']
    return txt
