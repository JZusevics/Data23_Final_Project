import json
import numpy
import pandas as pd
import id_extract
import cleaning_functions
import junction_table_creator
import df_transform

def clean(transformed_txt):
    extracted = extract_all()
    extracted_txt = extracted[2]
    clean_location(extracted_txt)
    split_names(extracted_txt)
    df = cand_id_gen_txt(extracted_txt)


    # fname = os.path.join("transformed_txt_with_full_name (1).csv")
    # generated_id = pd.read_csv(fname)

    desired_width=320
    pd.set_option('display.width', desired_width)
    numpy .set_printoptions(linewidth=desired_width)
    pd.set_option('display.max_columns', 10)

    f = open('data.json')
    candidate_json = json.load(f)


    f = open('data.json')
    candidate_json = json.load(f)
    date_format = "%d-%m-%Y"
    yes_no_keys = ['self_development', 'financial_support_self', 'geo_flex']
    candidate_json_keys = candidate_json.keys()
    candidate_json = cleaning_functions.json_cleaning(candidate_json, candidate_json_keys, date_format, yes_no_keys)
    # generates the skill id dataframes
    [strength_id, weakness_id, tech_skill_id] = id_extract.skill_id(candidate_json_keys, candidate_json)
    [strength_junc, weakness_junc, tech_skill_junc, candidate_json] = junction_table_creator.skill_junctions(candidate_json_keys,candidate_json)


    candidate_df = df_transform.transform_function(candidate_json_keys, candidate_json)


    columns = ['candidate_name']
    joined_df = candidate_df.join(transformed_txt.set_index(columns), lsuffix='_left', rsuffix='_right', on=columns, how='inner')


    joined_df = joined_df.sort_values(by=["applicant_day_date_right"].isnull())
    is_NaN = joined_df["applicant_day_date_left"].compare(joined_df["applicant_day_date_right"])
    print(is_NaN)



    # with open('data_clean.json', 'w') as fp:
    #     json.dump(candidate_json, fp, sort_keys=True, indent=4)
    #
    #
    # candidate_df.to_csv('df.csv', index=False)
    #
    # joined_df.to_csv('joined_df.csv', index=False)



