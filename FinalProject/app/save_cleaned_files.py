from Data23_Final_Project.FinalProject.app.cleaning_functions.clean_all_files import *
from Data23_Final_Project.FinalProject.app.extract_functions.extract_all import *
from pprint import pprint
import df_id_gen
import vrindas_join_functions
import df_id_append
import pandas as pd
import json

# extract all files
# extracted = extract_all()
with open('data.json') as f:
    extracted1 = json.loads(f.read())

extracted0 = pd.read_csv('academy.csv')
extracted2 = pd.read_csv('txt.csv')
extracted3 = pd.read_csv('talent.csv')
extracted = [extracted0, extracted1, extracted2, extracted3]



# clean all files
academy_csv, talent_json, talent_txt, talent_csv, json_skill_tables = clean_all_files(extracted)

#
# academy_csv.to_csv('transformed_academy_csv.csv')
# talent_json.to_csv('transformed_talent_json.csv')
# talent_txt.to_csv('transformed_talent_txt.csv')
# talent_csv.to_csv('transformed_talent_csv.csv')


talent_txt_merge = vrindas_join_functions.talent_csv_txt(talent_csv, talent_txt)
talent_academy_merge = vrindas_join_functions.talent_csv_json(talent_csv, academy_csv)
talent_json_merge = vrindas_join_functions.talent_csv_json(talent_csv, talent_json)
talent_json_merge.to_csv('transformed_academy_csv.csv')

strength_junc, weakness_junc, tech_self_score = df_id_append.id_replace_call(json_skill_tables, talent_json_merge)
talent_academy_merge, course_junc, course_info = df_id_gen.id_generator(talent_academy_merge)
