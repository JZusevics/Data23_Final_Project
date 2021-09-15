import pandas as pd

def spelling_clean_academy(df: pd.DataFrame):
    """

     :param df: csv dataframe generated from the extraction stage of the ETL pipeline
     :return: dataframe with correct spelling
     """
    df.trainer.replace("Ely Kely", "Elly Kelly", inplace=True)
    return df
