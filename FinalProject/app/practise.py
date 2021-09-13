from Data23_Final_Project.FinalProject.app.extract_functions.extract_all import *
from pprint import pprint
import pandas as pd
import numpy


def split_names(df: pd.DataFrame):
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
                        split_name = ["".join(split_name[split_name.index(sub_name):2])]+ split_name[2::]
                    if sub_name in split_name:
                        split_name = split_name[0:split_name.index(sub_name)]+[" ".join(split_name[split_name.index(sub_name)::])]

        first_name.append(split_name[0].title())
        last_name.append(split_name[-1].title())
        if len(split_name) == 2:
            middle_name.append(numpy.nan)
        else:
            middle_name.append("".join(split_name[1:-1]).title())

    df.insert(1, "first_name", first_name, True)
    df.insert(2, "middle_name", middle_name, True)
    df.insert(3, "last_name", last_name, True)
    df.drop(columns="name", inplace=True)
    return df


def cand_id_gen(scores: pd.DataFrame):
    scores["candidate_id"] = scores["first_name"]+" "+scores["last_name"] + " " + scores["date"].map(str)
    temp = scores[~scores["middle_name"].isna()]
    scores.loc[~scores["middle_name"].isna(), ["candidate_id"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp["last_name"] + " " + temp["date"].map(str)
    return scores[["candidate_id", "first_name", "middle_name", "last_name", "psychometrics_score", "presentation_score", "date", "location"]]


extracted = extract_all()
# pprint(extracted[0][0:5])
# pprint(extracted[1]['Zsa Zsa Rounsefull 16/07/2019'])
# pprint(extracted[2])
# pprint(extracted[3])

pprint(extracted[2])

cleaned_name = split_names(extracted[2])
pprint(cleaned_name.loc[:, ["first_name", "middle_name", "last_name"]])

id_generated = cand_id_gen(cleaned_name)
id_generated['name'] = id_generated["candidate_id"].map(lambda x: x[0:-11])
pprint(id_generated)

talent_csv = pd.read_csv('talent_csv.csv')
useful = talent_csv.loc[:, ["name", "invitation_date", "candidate_id"]]
no_date = useful[useful["invitation_date"].isna()]
pprint(list(no_date['name']))

for name in list(no_date['name']):
    df = id_generated[id_generated["name"] == name]
    if list(df['name']):
        pprint(df)
