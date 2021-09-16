from FinalProject.app.transform.cleaning_functions.join_names_csv import *
from FinalProject.app.transform.cleaning_functions.split_names import *
from FinalProject.app.transform.cleaning_functions.talent_csv_cleaning.clean_talent_csv import *
from FinalProject.app.transform.cleaning_functions.talent_csv_cleaning.spell_check_talent import *


def clean_talent_csv(df: pd.DataFrame):
    df = talent_csv_invite_date(df)
    df = talent_csv_dob(df)
    df = talent_csv_phone(df)
    df = talent_csv_column_names_erd(df)
    df = talent_csv_id_gen(df)
    df = split_names(df)
    df = full_name(df)
    df = spelling_clean_talent(df)
    return df
