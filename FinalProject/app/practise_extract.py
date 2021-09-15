from Data23_Final_Project.FinalProject.app.extract_functions.extract_all import *
from pprint import pprint
import pandas as pd
import numpy as np


def split_names(df: pd.DataFrame):
    last_name_prefix = ["Van", "Le", "Di", "O", "De", "Du", "Von", "St", "Mc", "Mac", "La"]
    first_name = []
    middle_name = []
    last_name = []

    df["name"] = df['name'].str.replace(" '", "'")
    df["name"] = df['name'].str.replace("' ", "'")
    df["name"] = df['name'].str.replace(" - ", "'")

    for name in df["name"]:
        # Split names on spaces
        split_name = name.split()
        for index, name in enumerate(split_name):
            split_name[index] = name.title()
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
                        split_name = ["".join(split_name[split_name.index(sub_name):2])]+ split_name[2::]
                    if sub_name in split_name:
                        split_name = split_name[0:split_name.index(sub_name)]+[" ".join(split_name[split_name.index(sub_name)::])]

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


def cand_id_gen_txt(scores: pd.DataFrame):
    scores["candidate_id_str"] = scores["first_name"]+" "+scores["last_name"] + " " + scores["date"].map(str)
    temp = scores[~scores["middle_name"].isnull()]
    scores.loc[~scores["middle_name"].isna(), ["candidate_id_str"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp["last_name"] + " " + temp["date"].map(str)
    scores = scores[["candidate_id_str", "first_name", "middle_name", "last_name", "psychometrics_score", "presentation_score", "date", "location"]]
    return scores


def clean_location(df: pd.DataFrame):
    df["location"] = df["location"].map(lambda x: x.replace(" Academy", ""))

extracted = extract_all()
extracted_txt = extracted[2]
pprint(extracted_txt)

# clean talent txt
clean_location(extracted_txt)
split_names(extracted_txt)
cand_id_gen_txt(extracted_txt)
extracted_txt.to_csv("transformed_talent_txt.csv")

# clean talent csv
talent_csv_extracted = extracted[3]
converted_date = talent_csv_invite_date(talent_csv_extracted)
converted_dob = talent_csv_dob(converted_date)
converted_phone = talent_csv_phone(converted_dob)
cleaned = talent_csv_column_names_erd(converted_phone)
gen_id = talent_csv_id_gen(cleaned)
cleaned_names = split_names(gen_id)
cleaned_names.to_csv("talent_cleaned.csv")
pprint(cleaned_names)
