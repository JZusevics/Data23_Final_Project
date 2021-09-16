from FinalProject.app.transform.cleaning_functions.cleaning_academy_csv.spell_check_academy import *
from FinalProject.app.transform.cleaning_functions.split_names import *
from FinalProject.app.transform.cleaning_functions.join_names_csv import *


def clean_academy_csv(df: pd.DataFrame):
    df = split_names(df)
    df = full_name(df)
    df = spelling_clean_academy(df)
    return df
