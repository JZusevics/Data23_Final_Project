from Data23_Final_Project.FinalProject.app.cleaning_functions.academy_csv_cleaning.spell_check_academy import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.split_names import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.join_names_csv import *


def clean_academy_csv(df: pd.DataFrame):
    df = split_names(df)
    df = full_name(df)
    df = spelling_clean_academy(df)
    return df
