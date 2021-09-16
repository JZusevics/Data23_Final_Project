from FinalProject.app.transform.cleaning_functions.cleaning_academy_csv.clean_all_academy_csv import *
from FinalProject.app.transform.cleaning_functions.id_into_txt import *
from FinalProject.app.transform.cleaning_functions.talent_csv_cleaning.clean_all_talent_csv import *
from FinalProject.app.transform.cleaning_functions.talent_json_cleaning.json_cleaning_main import *
from FinalProject.app.transform.cleaning_functions.talent_txt_cleaning.clean_all_txt import *
from FinalProject.app.transform.cleaning_functions.fix_mismatched_dates import *
# Paula, DW about it >:)
pd.options.mode.chained_assignment = None

def clean_all_files(extracted: list):
    # clean all files
    academy_csv = clean_academy_csv(extracted[0])

    cleaned_json = clean_json(extracted[1])
    talent_json = cleaned_json[0]
    skill_tables = cleaned_json[1:]
    talent_txt = clean_txt(extracted[2])
    print(talent_txt)
    talent_csv = clean_talent_csv(extracted[3])
    # add candidate_id to talent_txt
    talent_txt = candidate_id_into_txt(talent_csv, talent_txt)
    # update incorrect dates
    talent_json = update_incorrect_dates(talent_json, talent_csv)

    return academy_csv, talent_json, talent_txt, talent_csv, skill_tables
