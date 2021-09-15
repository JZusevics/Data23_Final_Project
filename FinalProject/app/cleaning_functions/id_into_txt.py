import pandas as pd


def candidate_id_into_txt(csv: pd.DataFrame, txt: pd.DataFrame):
    """
    :param csv: csv dataframe generated from the extraction stage of the ETL pipeline
    :param txt: txt dataframe generated from the extraction stage of the ETL pipeline
    :return: txt dataframe with candidate_id columns that match the csv candidate_id column
    """
    # txt['applicant_day_date'] = txt['date']  # change name in text table so you have uniform columns names
    # use a join to get the correct ids for each candidate
    new = pd.merge(txt, csv, on=['candidate_name', 'applicant_day_date'], how='outer')

    # add this into the txt dataframe
    connection = new[~new['candidate_id_str'].isna()].loc[:, ['candidate_id_str', 'candidate_id']]
    txt = pd.merge(txt, connection, on=['candidate_id_str'], how='outer')
    return txt
