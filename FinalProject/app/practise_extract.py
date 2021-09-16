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

json_txt_joined = pd.merge(talent_txt, talent_json, on=['candidate_name'], how='outer')
dupe_names = json_txt_joined[json_txt_joined['candidate_name'].duplicated(keep=False)]
incorrect_dupes = dupe_names[dupe_names['applicant_day_date_x'].astype(str) != dupe_names['applicant_day_date_y'].astype(str)]
dropped_dupes = json_txt_joined.drop(index=list(incorrect_dupes.index))

# mismatched_dates = dropped_dupes[~(dropped_dupes['applicant_day_date_x'].astype(str) == dropped_dupes['applicant_day_date_y'].astype(str))]
# wrong_dates = mismatched_dates[~mismatched_dates['applicant_day_date_x'].isna()]
# correct_json_dates = wrong_dates.loc[:, ['candidate_name', 'applicant_day_date_y']]
# # names_to_change_dates = wrong_dates['candidate_name'].tolist()
#
# matched_dates = dropped_dupes[(dropped_dupes['applicant_day_date_x'].astype(str) == dropped_dupes['applicant_day_date_y'].astype(str))]
# original_matched_dates = matched_dates.loc[:, ['candidate_name', 'applicant_day_date_y']]
# updated_dates = pd.concat([correct_json_dates, original_matched_dates]).rename(columns={'applicant_day_date_y': 'applicant_day_date'})
# dropped_old_dates = talent_json.drop(columns=['applicant_day_date'])
# talent_json_new_dates = pd.merge(dropped_old_dates, updated_dates, on=['candidate_name'], how='inner')
#
# json_txt_joined_updated_dates = pd.merge(talent_json_new_dates, talent_csv, on=['candidate_name', 'applicant_day_date'], how='outer')

# sparta_skill_dict = {'sparta_skill_id': [1, 2, 3, 4, 5, 6], 'skill_name': ['analytic', 'independent', 'determined',
#                                                                            'professional', 'studious', 'imaginative']}
# sparta_skill = pd.DataFrame(sparta_skill_dict)
#
# skill_link = {'analytic': 1, 'independent': 2, 'determined': 3, 'professional': 4, 'studious': 5, 'imaginative': 6}
#
# academy_csv_txt_joined = pd.merge(academy_csv, talent_txt, on=['candidate_name'], how='inner')
# # compare_dates = academy_csv_txt_joined.loc[:, ['candidate_id', 'candidate_name', 'applicant_day_date', 'course_start_date']]
# renamed = academy_csv_txt_joined.rename(columns={'candidate_id': 'temp_candidate_id'})
# renamed.insert(7, 'candidate_id', renamed['temp_candidate_id'])
# useful = renamed.iloc[:, 7:68]
#
#
# cand_ids = []
# weeks = []
# skills = []
# scores = []
#
# for index, row in useful.iterrows():
#     for col in row.index:
#         if col != 'candidate_id' and not np.isnan(row[col]):
#             dash_index = col.index("_")
#             skill_id = skill_link[col[:dash_index].lower()]
#             week = col[dash_index+2:]
#             cand_ids.append(int(row['candidate_id']))
#             weeks.append(int(week))
#             skills.append(int(skill_id))
#             scores.append(int(row[col]))
#
# academy_performance_dict = {'candidate_id': cand_ids, 'week': weeks, 'sparta_skill_id': skills, 'score': scores}
# academy_performance = pd.DataFrame(academy_performance_dict)
#
# sparta_skills = set()
# for col in useful.columns:
#     dash_index = col.index("_")
#     skill = col[:dash_index].lower()
#     sparta_skills.add(skill)
# sparta_skills.remove('candidate')
