from FinalProject.app.transform.cleaning_functions.split_names import *
from FinalProject.app.transform.cleaning_functions.talent_txt_cleaning.generate_id import *
from FinalProject.app.transform.cleaning_functions.talent_txt_cleaning.remove_academy import *


def clean_txt(df: pd.DataFrame):
    df = clean_location(df)
    df = split_names(df)
    df = cand_id_gen_txt(df)
    return df
