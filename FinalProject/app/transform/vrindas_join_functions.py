
import pandas as pd

def talent_csv_txt(df: pd.DataFrame, txt: pd.DataFrame):
    talent_txt_merge = pd.merge(df, txt, on=['candidate_name', 'applicant_day_date'], how='outer', indicator=True)
    return talent_txt_merge

def talent_csv_json(df: pd.DataFrame, json: pd.DataFrame):
    talent_json_merge = pd.merge(df, json, on="candidate_name", how='outer', indicator=True)
    return talent_json_merge
