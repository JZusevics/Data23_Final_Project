import pandas as pd


def clean_location(df: pd.DataFrame):
    df["location"] = df["location"].map(lambda x: x.replace(" Academy", ""))
    return df
