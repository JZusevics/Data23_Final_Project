from Data23_Final_Project.FinalProject.app.cleaning_functions.clean_all_files import *
from Data23_Final_Project.FinalProject.app.extract_functions.extract_all import *
from pprint import pprint


# extract all files
extracted = extract_all()

# clean all files
academy_csv, talent_json, talent_txt, talent_csv, json_skill_tables = clean_all_files(extracted)

academy_csv.to_csv('transformed_academy_csv.csv')
talent_json.to_csv('transformed_talent_json.csv')
talent_txt.to_csv('transformed_talent_txt.csv')
talent_csv.to_csv('transformed_talent_csv.csv')
