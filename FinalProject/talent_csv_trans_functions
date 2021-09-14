import numpy as np
import pandas as pd


def talent_csv_invite_date(df):  # dealing with the invitation date
    """

    :param df: dataframe generated from the extraction stage of the ETL pipeline
    :return: invitation date transformed into datetime format
    """
    df["date_int"] = df.invited_date.astype(str)
    df[["split_date", "dot"]] = df.date_int.str.split(".", 1, edfpand=True)
    df["invitation_date"] = df.split_date + " " + df.month.str.lower()
    # splits month column into split_month and split_year - adds at end of df
    df[["split_month", "split_year"]] = df.month.str.split(" ", 1, edfpand=True)
    # sets any NaN that was converted to string back to NaN format
    df.split_date.replace("nan", np.nan, inplace=True)
    # keeps only first 3 characters from the months & converts to title format for datetime
    df["sliced_month"] = df.split_month.str.slice(stop=3).str.title()
    # combining the columns to form the date
    df["applicant_day_date"] = df.split_year + "-" + df.sliced_month + "-" + df.split_date
    df["applicant_day_date"] = pd.to_datetime(df["applicant_day_date"], format='%Y-%b-%d')
    # pop out any unwanted columns
    df.pop("dot")
    df.pop("date_int")
    df.pop("invited_date")
    df.pop("month")
    df.pop("split_month")
    df.pop("split_date")
    df.pop("sliced_month")
    df.pop("split_year")
    df.pop("invitation_date")

    return df


# dealing with date of birth - change format to sql datetime format
def talent_csv_dob(df):
    """

    :param df: dataframe generated from the extraction stage of the ETL pipeline
    :return: SQL formal of date of birth
    """
    df["dob"] = pd.to_datetime(df["dob"], format='%d/%m/%Y')  # use datetime to change format
    df["date_of_birth"] = df.dob  # change name for consistency
    df.pop("dob")

    return df


# dealing with phone numbers being in different formats
def talent_csv_phone(df):
    """

    :param df: dataframe generated from the extraction stage of the ETL pipeline
    :return: dataframe with no "-" or " " in mobile phone numbers, where available
    """
    # fill na to make workable
    df.phone_number = df.phone_number.fillna('')
    # getting rid of characters that are unwanted
    df.phone_number = df.phone_number.str.replace("(", "").str.replace(")", "").str.replace(" ", "-").str.replace("-", "")
    # turning missing data into nan
    df.phone_number.replace("", np.nan, inplace=True)

    return df


# we have column names/data types that do not match the ERD so this will deal with this
def talent_csv_column_names_erd(df):
    """

    :param df: dataframe generated from the extraction stage of the ETL pipeline
    :return: dataframe with correct column names and data types as specified in the ERD
    """
    # email it in float and we need it in string
    df["email"] = df.email.astype(str)
    # need "university" not "uni"
    df["university"] = df.uni.astype(str)
    df.pop("uni")
    # need "applicant_day_trainee_id" not "id"
    df["applicant_day_trainee_id"] = df.id.astype(int)
    df.pop("id")
    # need "invited_by_name" not "invited_by"
    df["invited_by_name"] = df.invited_by.astype(str)
    df.pop("invited_by")

    return df
