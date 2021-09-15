import pandas as pd
import numpy as np


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


def split_names(df):
    """
    Fixes name format in files
    """
    last_name_prefix = ["Van", "Le", "Di", "O", "De", "Du", "Von", "St", "Mc", "Mac", "La"]
    first_name = []
    middle_name = []
    last_name = []

    for name in df["name"]:
        # Split names on spaces
        split_name = name.split()
        # If more than 2 names
        if len(split_name) > 2:
            # If the first name and second name are the same put them together
            if split_name[0] == split_name[1]:
                split_name = [" ".join(split_name[0:2])] + split_name[2:]
            # If name contains a prefix put the following names together
            for sub_name in last_name_prefix:
                if sub_name in split_name:
                    # Check if prefix is in the first name only put first and second together
                    if split_name.index(sub_name) == 0:
                        split_name = ["".join(split_name[split_name.index(sub_name):2])] + split_name[2::]
                    if sub_name in split_name:
                        split_name = split_name[0:split_name.index(sub_name)] + [
                            " ".join(split_name[split_name.index(sub_name)::])]

        first_name.append(split_name[0].title())
        last_name.append(split_name[-1].title())
        if len(split_name) == 2:
            middle_name.append(np.nan)
        else:
            middle_name.append("".join(split_name[1:-1]).title())

    df.insert(1, "first_name", first_name, True)
    df.insert(2, "middle_name", middle_name, True)
    df.insert(3, "last_name", last_name, True)
    df.drop(columns="name", inplace=True)
    return df


def cand_id_gen(df):
    """
    creates a fixed middle name format for file joining
    """
    df["candidate_name"] = df["first_name"] + " " + df["last_name"].map(str)
    temp = df[~df["middle_name"].isnull()]
    df.loc[~df["middle_name"].isna(), ["candidate_name"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp[
        "last_name"].map(str)
    return df
