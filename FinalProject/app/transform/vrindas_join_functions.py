
import pandas as pd

# functiona to merge files

def talent_csv_txt(df: pd.DataFrame, txt: pd.DataFrame):
    """
    
    :param df: csv dataframe generated from the extraction stage of the ETL pipeline
    :param txt: txt dataframe generated from the extraction stage of the ETL pipeline
    :return: df and txt dataframes merged on df
    """
    talent_txt_merge = pd.merge(df, txt, on=['candidate_name', 'applicant_day_date'], how='outer', indicator=True)
    return talent_txt_merge

def talent_csv_json(df: pd.DataFrame, json: pd.DataFrame):
    """

    :param df: csv dataframe generated from the extraction stage of the ETL pipeline
    :param json: json dataframe generated from the extraction stage of the ETL pipeline
    :return: df and json dataframes merged on df
    """
    talent_json_merge = pd.merge(df, json, on="candidate_name", how='outer', indicator=True)
    return talent_json_merge
