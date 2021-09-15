import pandas as pd


def skill_id_generator(name_dates, skill, candidate_json):
    """
    Generates all of the skill ids for the skill id tables
    """
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


def tech_skill_id_generator(name_dates, skill, candidate_json):
    """
    Generates all of the skill ids for the tech skill id tables
    """
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
        i = i + 1
    for candidate in name_dates:
        try:
            strengths = candidate_json[candidate][skill]
            for strength in list(strengths):
                candidate_json[candidate][skill][strengths_id[strength]] = candidate_json[candidate][skill][
                    strength]
                del candidate_json[candidate][skill][strength]
        except KeyError:
            pass
    strengths_id = {value: key for key, value in strengths_id.items()}
    return strengths_id


def table_creator(dict, table_name, index_name):
    """
    turns table dictionaries into data frames
    """
    dataframe = pd.Series(dict, name=table_name)
    dataframe.index.name = index_name
    dataframe.reset_index()
    dataframe = pd.DataFrame(dataframe)
    return dataframe


def skill_id(candidate_json_keys, candidate_json):
    """
    runs all function in id_extract
    """

    strength_id = skill_id_generator(candidate_json_keys, 'strengths', candidate_json)
    weakness_id = skill_id_generator(candidate_json_keys, 'weaknesses', candidate_json)
    tech_skill_id = tech_skill_id_generator(candidate_json_keys, 'tech_self_score', candidate_json)
    strength_df = table_creator(strength_id, 'strength_ids_df', 'strength_id')
    weakness_df = table_creator(weakness_id, 'weakness_ids_df', 'weakness_id')
    tech_skill_df = table_creator(tech_skill_id, 'tech_skill_ids_df', 'tech_skill_id')
    return strength_df, weakness_df, tech_skill_df