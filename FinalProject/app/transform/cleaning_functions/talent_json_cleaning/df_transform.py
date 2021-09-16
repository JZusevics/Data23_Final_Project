import numpy as np
import pandas as pd
from FinalProject.app.transform.cleaning_functions.split_names import *

def transform_function(candidate_json_keys, candidate_json):
    """
    runs all functions in df_transform
    """
    candidate_json = key_remover(candidate_json_keys, candidate_json)
    candidate_df = pd.DataFrame(candidate_json)
    df = split_names(candidate_df)
    df = cand_id_gen(df)
    return df


def key_remover(candidate_json_keys, candidate_json):
    """
    removes extracted data from json
    """
    list_obj = []
    for key in list(candidate_json_keys):
        # print(candidate_json[name])
        del candidate_json[key]['strengths']
        del candidate_json[key]['weaknesses']
        try:
            del candidate_json[key]['tech_self_score']
        except KeyError:
            pass
        list_obj.append(candidate_json[key])
    return list_obj


def cand_id_gen(df):
    """
    creates a fixed middle name format for file joining
    """
    df["candidate_name"] = df["first_name"] + " " + df["last_name"].map(str)
    temp = df[~df["middle_name"].isnull()]
    df.loc[~df["middle_name"].isna(), ["candidate_name"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp[
        "last_name"].map(str)
    return df
