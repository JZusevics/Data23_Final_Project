import pandas as pd

def invited_spelling_talent(df: pd.DataFrame):
    """
    
    :param df: csv dataframe generated from the extraction stage of the ETL pipeline
    :return: dataframe with correct spelling
    """
    for item in df.invited_by_name:
        if item == "Fifi Eton":
            item = "Fifi Etton"
        if item == "Belbrook":
            item = "Bellbrook"
    return df
