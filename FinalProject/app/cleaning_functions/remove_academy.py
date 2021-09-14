import pandas as pd


def clean_location(df: pd.DataFrame):
    df["Location"] = df["Location"].map(lambda x: x.replace(" Academy", ""))
    return df