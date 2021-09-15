from Data23_Final_Project.FinalProject.app.extract_functions.extract_all import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_csv_cleaning.clean_all_talent_csv import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_txt_cleaning.clean_all_txt import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.academy_csv_cleaning.clean_all_academy_csv import *


# extract all files
extracted = extract_all()

# clean academy csv
academy_csv = clean_academy_csv(extracted[0])

# clean talent txt
talent_txt = clean_txt(extracted[2])

# clean talent csv
talent_csv = clean_talent_csv(extracted[3])


# extracted = extract_all()
#
# extracted_txt = extracted[2]
# step1 = clean_location(extracted_txt)
# step2 = split_names(step1)
# transformed_txt = cand_id_gen_txt(step2)
#
# talent_csv_extracted = extracted[3]
# converted_date = talent_csv_invite_date(talent_csv_extracted)
# converted_dob = talent_csv_dob(converted_date)
# converted_phone = talent_csv_phone(converted_dob)
# cleaned = talent_csv_column_names_erd(converted_phone)
# gen_id = talent_csv_id_gen(cleaned)
# cleaned_names = split_names(gen_id)
# full_name = full_name(cleaned_names)
# spell_checked = spelling_clean_talent(full_name)
#
# join = candidate_id_into_txt(full_name, transformed_txt)