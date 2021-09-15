def full_name(df):
    """
    :param df: csv dataframe generated from the extraction stage of the ETL pipeline
    :return: dataframe with a column for full_name joined from first_name, middle_name and last_name again
    """
    df["candidate_name"] = df["first_name"] + " " + df["last_name"].map(str)
    temp = df[~df["middle_name"].isnull()]
    df.loc[~df["middle_name"].isna(), ["candidate_name"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp[
        "last_name"].map(str)
    return df
