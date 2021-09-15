import pandas as pd

def spelling_clean_talent(df: pd.DataFrame):
    """

    :param df: csv dataframe generated from the extraction stage of the ETL pipeline
    :return: dataframe with correct spelling
    """
    df.invited_by_name.replace("Fifi Eton", "Fifi Etton", inplace=True)
    df.invited_by_name.replace("Belbrook", "Bellbrook", inplace=True)
    return df
