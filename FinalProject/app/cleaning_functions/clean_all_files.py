from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_csv_cleaning.clean_all_talent_csv import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_txt_cleaning.clean_all_txt import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.academy_csv_cleaning.clean_all_academy_csv import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.id_into_txt import *


def clean_all_files(extracted: list):

    # clean all files
    academy_csv = clean_academy_csv(extracted[0])

    talent_txt = clean_txt(extracted[2])
    talent_csv = clean_talent_csv(extracted[3])

    # add candidate_id to talent_txt
    talent_txt = candidate_id_into_txt(talent_csv, talent_txt)
    return academy_csv, talent_txt, talent_csv

