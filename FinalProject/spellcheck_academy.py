import pandas as pd

def trainer_spelling_academy(df: pd.DataFrame):
    """

     :param df: csv dataframe generated from the extraction stage of the ETL pipeline
     :return: dataframe with correct spelling
     """
    for item in df.trainer:
        if item == "Ely Kely":
            item = "Elly Kelly"
    return df
