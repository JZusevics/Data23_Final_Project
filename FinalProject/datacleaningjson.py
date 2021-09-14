import json
import datetime
import numpy
import pandas as pd
import os
import csv


fname = os.path.join("connor.csv")
generated_id = pd.read_csv(fname)

desired_width=320
pd.set_option('display.width', desired_width)
numpy .set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

f = open('data.json')
candidate_json = json.load(f)


def internal_id_append(json_keys, json):
    """
    This Creates an internal id for creation of data frame, so that all data can be referenced and have a new id assigned
    :param json_keys: Keys that point to each json in the json file
    :param candidate_json: Json file of candidate date
    :return: Json files updated with a candidate key selection
    """
    candidate_id = 0
    for name in list(json_keys):
        json[name]['internal_id'] = candidate_id
        candidate_id += 1
    return json


def date_test(name_dates, format, candidate_json):
    """
    Test that the dates are in a datetime format, then rearranges them to match our sql format
    Tests that dates are
    :param name_dates: Keys for iterating through the json file
    :param format: The date format the original dates should be in
    :param candidate_json: The json of all of the candidate date
    :return: candidate-json with and updated date format
    """
    for candidate in name_dates:
        # replaces / characters with - for sql
        date = candidate_json[candidate]['date']
        date = date.replace('/', '-')
        # try and except loop to stop breaks when key is not found in json
        try:
            date = datetime.datetime.strptime(date, format).strftime("%Y-%m-%d")
            candidate_json[candidate]['date'] = date
            candidate_json[candidate]['applicant_day_date'] = candidate_json[candidate]['date']
            del candidate_json[candidate]['date']
        except ValueError:
            # fixes standard error of too many dashes
             date = date.replace('-', '', 1)
             try:
                 date = datetime.datetime.strptime(date, format).strftime("%Y-%m-%d")
                 candidate_json[candidate]['date'] = date
                 candidate_json[candidate]['applicant_day_date'] = candidate_json[candidate]['date']
                 del candidate_json[candidate]['date']
             except ValueError:
                print("Value error date ", date, " not in correct format")

    return candidate_json


def bool_fix(name_dates, candidate_json, yes_no_key):
    """
    Test that bool the three boolean key date pairs of financial_support_self, geo_flex and self_development are true
    :param name_dates: Keys for iterating through the json file
    :param candidate_json: the json of all of the candidate date
    :param yes_no_key: List of three keys we are testing
    :return:
    """
    for candidate in name_dates:
        for key in yes_no_keys:
            test = str(candidate_json[candidate][key].strip())
            if test == 'Yes' or test == 'yes' or test == 'Y' or test == 'y':
                candidate_json[candidate][key] = True
            elif test == 'No' or test == 'no' or test == 'N' or test == 'n':
                candidate_json[candidate][key] = False
            else:
                # returns incorrect data for error exploration
                print(test)
    return candidate_json


def results_fix(name_dates, candidate_json):
    """
    Changes the results key to pass and converts pass or fail to true or false to enable boolean or bit logic
    :param name_dates:
    :param candidate_json:
    :return: Updated candidate_json
    """
    for candidate in name_dates:
        test = str(candidate_json[candidate]['result'])
        candidate_json[candidate]['pass'] = candidate_json[candidate]['result']
        del candidate_json[candidate]['result']
        if test == 'Pass':
            candidate_json[candidate]['pass'] = True
        elif test == 'Fail':
            candidate_json[candidate]['pass'] = False
        else:
            # returns incorrect data for error exploration
            print(test)
    return candidate_json


def name_strip(name_dates ,candidate_json):
    """
    Strips white space off of names, might not be nesaccary
    :param name_dates:
    :param candidate_json:
    :return:
    """
    for candidate in name_dates:
        candidate_json[candidate]['name'] = str(candidate_json[candidate]['name']).strip().lower().title()
        # code commented out can be used to check for incorrect name formats
        # if str(candidate_json[candidate]['name']).strip().lower().title().count(' ') > 1:
        # print(str(candidate_json[candidate]['name']).strip().lower().title())
    return candidate_json


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


def skill_id_generator(name_dates, skill):
    list_strengths = []
    for candidate in name_dates:
        strengths = candidate_json[candidate][skill]
        for strength in strengths:
            if strength not in list_strengths:
                list_strengths.append(strength)
        i = 1
    strengths_id = {}
    for strength in list_strengths:
        strengths_id.update({strength: i})
        i += 1
    for candidate in name_dates:
        strengths = candidate_json[candidate][skill]
        for i, strength in enumerate(strengths):
            id = strengths_id[strength]
            candidate_json[candidate][skill][i] = id
    strengths_id = {value: key for key, value in strengths_id.items()}
    return strengths_id


def tech_skill_id_generator(name_dates, skill):
    list_strengths = []
    for candidate in name_dates:
        try:
            strengths = candidate_json[candidate][skill]
            for strength in strengths:
                if strength not in list_strengths:
                    list_strengths.append(strength)
        except KeyError:
            pass
    i = 1
    strengths_id = {}
    for strength in list_strengths:
        strengths_id.update({strength: i})
        i = i+1
    for candidate in name_dates:
        try:
            strengths = candidate_json[candidate][skill]
            for strength in list(strengths):
                candidate_json[candidate][skill][strengths_id[strength]] = candidate_json[candidate][skill][strength]
                del candidate_json[candidate][skill][strength]
        except KeyError:
           pass
    strengths_id = {value: key for key, value in strengths_id.items()}
    return strengths_id


def table_creator(dict, table_name, index_name):
    dataframe = pd.Series(dict, name=table_name)
    dataframe.index.name = index_name
    dataframe.reset_index()
    return dataframe


def strengths_candidate_id_creator(json_keys, json, key):
    """
    Creates a data frame with one column
    :param json_keys:
    :param json:
    :param key:
    :return:
    """
    df_list = []
    for name in json_keys:
        try:
            for item in json[name][key]:
                df_list.append([json[name]['internal_id'], item])
        except KeyError:
            pass
    df = pd.DataFrame(df_list, columns=['id','skill'])
    return df


def cand_id_gen(scores: pd.DataFrame):
    scores["candidate_name"] = scores["first_name"]+" "+scores["last_name"] # + " " + scores["applicant_day_date"].map(str)
    temp = scores[~scores["middle_name"].isna()]
    scores.loc[~scores["middle_name"].isna(), ["candidate_name"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp["last_name"] # + " " + temp["applicant_day_date"].map(str)
    return scores[["candidate_name", "course_interest", "first_name", "middle_name", "last_name", "financial_support_self", "geo_flex", "self_development", "internal_id", "applicant_day_date", "pass"]]


yes_no_keys = ['self_development', 'financial_support_self', 'geo_flex']
candidate_json_keys = candidate_json.keys()
date_format = "%d-%m-%Y"


internal_id_append(candidate_json_keys, candidate_json)
candidate_json = name_strip(candidate_json_keys, candidate_json)
candidate_json = date_test(candidate_json_keys, date_format, candidate_json)
candidate_json = bool_fix(candidate_json_keys, candidate_json, yes_no_keys)
candidate_json = results_fix(candidate_json_keys, candidate_json)
strengths_id = skill_id_generator(candidate_json_keys, 'strengths')
weakness_id = skill_id_generator(candidate_json_keys, 'weaknesses')
tech_skill_id = tech_skill_id_generator(candidate_json_keys, 'tech_self_score')
strength_ids_df = table_creator(strengths_id, 'strength_ids', 'Strength_id')
weakness_ids_df = table_creator(weakness_id, 'weakness_ids_df', 'weakness_id')
tech_skill_ids_df = table_creator(tech_skill_id, 'tech_skill_ids_df', 'tech_skill_id')
strength_table= strengths_candidate_id_creator(candidate_json_keys, candidate_json, 'strengths')
weaknesses_table = strengths_candidate_id_creator(candidate_json_keys, candidate_json,'tech_self_score')
tech_skill_table = strengths_candidate_id_creator(candidate_json_keys, candidate_json,'weaknesses')


list_obj = []
for key in list(candidate_json_keys):
    #print(candidate_json[name])
    del candidate_json[key]['strengths']
    del candidate_json[key]['weaknesses']
    try:
        del candidate_json[key]['tech_self_score']
    except KeyError:
        pass
    list_obj.append(candidate_json[key])
candidate_df = pd.DataFrame(list_obj)

df = split_names(candidate_df)
df = cand_id_gen(df)
print(df)
columns = ['candidate_name', 'applicant_day_date']
joined_df = df.join(generated_id.set_index(columns), on=columns, how='inner')
print(joined_df)


with open('data_clean.json', 'w') as fp:
    json.dump(candidate_json, fp, sort_keys=True, indent=4)


df.to_csv('df.csv', index=False)

# joined_df.to_csv('joined_df.csv', index=False)



