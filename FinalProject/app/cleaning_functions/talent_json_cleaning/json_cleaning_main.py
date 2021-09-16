from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_json_cleaning.id_extract import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_json_cleaning.junction_table_creator import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_json_cleaning.json_cleaning_functions import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_json_cleaning.df_transform import *


def clean_json(candidate_json):
    """
    Main file for running the json cleaning and transformation
    """
    desired_width = 320
    pd.set_option('display.width', desired_width)
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 16)
    date_format = "%d-%m-%Y"
    yes_no_keys = ['self_development', 'financial_support_self', 'geo_flex']
    candidate_json_keys = candidate_json.keys()
    candidate_json = json_cleaning(candidate_json, candidate_json_keys, date_format, yes_no_keys)
    [strength_id, weakness_id, tech_skill_id] = skill_id(candidate_json_keys, candidate_json)
    [strength_junc, weakness_junc, tech_skill_junc, candidate_json] = skill_junctions(candidate_json_keys, candidate_json)
    candidate_df = transform_function(candidate_json_keys, candidate_json)
    return candidate_df, strength_id, weakness_id, tech_skill_id, strength_junc, weakness_junc, tech_skill_junc
