from FinalProject.app.transform.clean_json import clean_json
from FinalProject.app.load.schema_functions import *
from FinalProject.app.load.loading_functions import *

if __name__ == '__main__':

    reset_schema()
    #extract_just_json()
    strengths_junc_df, weakness_junc_df, tech_self_score_df = clean_json()
    print(tech_self_score_df)
    load_strength(strengths_junc_df)
    load_weakness(weakness_junc_df)
    load_tech_skill(tech_self_score_df)
    pass;
