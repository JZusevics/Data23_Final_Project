import pandas as pd

def check_email(df: pd.DataFrame):
    """

    :param df: talent csv dataframe generated from the extraction stage of the ETL pipeline
    :return: list of incorrect emails which can be used to query SQL dataset to find contact info
    """
    contact = []
    for email in df.email:
        if email != "nan": # need to make sure this is not because email does not exist
            if ("@" not in email) or ("." not in email):
                contact.append(email)
    return contact
