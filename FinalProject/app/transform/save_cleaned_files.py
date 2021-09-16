from FinalProject.app.transform.clean_all_files import *
from FinalProject.app.extract.extract_all import *
from pprint import pprint
from FinalProject.app.load.loading_functions import *
from FinalProject.app.transform.cleaning_functions.generate_academy_performance_dfs import *
from FinalProject.app.load.schema_functions import *
import FinalProject.app.transform.vrindas_join_functions as vrindas_join_functions
import FinalProject.app.transform.df_id_append as df_id_append
import FinalProject.app.transform.df_id_gen as df_id_gen
import FinalProject.app.transform.tables_sparta_day as tables_sparta_day


reset_schema('../../schema.txt')

with open('../../data.json') as f:
    extracted1 = json.loads(f.read())
extracted0 = pd.read_csv('../../academy.csv')
extracted2 = pd.read_csv('../../txt.csv')
extracted3 = pd.read_csv('../../talent.csv')
extracted = [extracted0, extracted1, extracted2, extracted3]



def clean_and_load(extracted):
    # clean all files
    print('Now cleaning...')
    academy_csv, talent_json, talent_txt, talent_csv, json_skill_tables = clean_all_files(extracted)

    talent_txt_merge = vrindas_join_functions.talent_csv_txt(talent_csv, talent_txt)
    talent_academy_merge = vrindas_join_functions.talent_csv_json(talent_csv, academy_csv)
    talent_json_merge = vrindas_join_functions.talent_csv_json(talent_csv, talent_json)
    talent_json_merge.to_csv('transformed_academy_csv.csv')

    strength_junc, weakness_junc, tech_self_score = df_id_append.id_replace_call(json_skill_tables, talent_json_merge)
    talent_academy_merge, course_junc, course_info = df_id_gen.id_generator(talent_academy_merge)
    inviter, talent_csv, trainer, academy_performance, talent = df_id_gen.trainer_inviter_table_creator(academy_csv, talent_csv)
    sparta_day, applicant_day_date, test_location, talent_txt_merge = tables_sparta_day.sparta_day_extract(talent_txt_merge)
    talent_txt_copy = talent_txt.loc[:,:]
    sparta_day_performance = tables_sparta_day.create_sparta_day_performance(talent_txt_copy, talent_json)

    candidate_info = vrindas_join_functions.talent_csv_json(academy_performance[['candidate_name', 'trainer_id']], talent)
    candidate_info = candidate_info[['candidate_id', 'inviter_id', 'trainer_id', 'applicant_day_trainee_id', 'first_name', 'middle_name','last_name', 'date_of_birth', 'gender', 'phone_number', 'university', 'degree', 'address', 'city', 'postcode', 'email']]

    talent_csv1 = talent_csv.where(pd.notnull(talent_csv), None)
    candidate_info1 = candidate_info.where(pd.notnull(candidate_info), None)
    sparta_day_performance1 = sparta_day_performance.where(pd.notnull(sparta_day_performance), None)
    test_location1 = test_location.where(pd.notnull(test_location), 'NaN')

    sparta_skill, academy_performance = create_academy_performance(academy_csv, talent_csv)
    print('Cleaning done')


    # print('0/16 | loading sparta_skill..')
    # load_sparta_skill(sparta_skill)
    # print('loaded')
    # print('1/16 | loading academy_performance..')
    # load_academy_performance(academy_performance)
    # print('loaded')
    # print('2/16 | loading candidate_info..')
    # load_candidate_info(candidate_info1)
    # print('loaded')
    # print('3/16 | loading inviter..')
    # load_inviter(inviter)
    # print('loaded')
    # print('4/16 | loading trainer..')
    # load_trainer(trainer)
    # print('loaded')
    # print('5/16 | loading sparta_day..')
    # load_sparta_day(sparta_day)
    # print('loaded')
    # print('6/16 | loading applicant_day_date..')
    # load_applicant_day_date(applicant_day_date)
    # print('loaded')
    # print('7/16 | loading test_location..')
    # load_test_location(test_location1)
    # print('loaded')
    # print('8/16 | loading weakness..')
    # load_weakness(json_skill_tables[1])
    # print('loaded')
    # print('9/16 | loading weakness_junc..')
    # load_weakness_junc(weakness_junc)
    # print('loaded')
    # print('10/16 | loading tech_skill..')
    # load_tech_skill(json_skill_tables[2])
    # print('loaded')
    # print('11/16 | loading tech_self_score..')
    # load_tech_self_score(tech_self_score)
    # print('loaded')
    # print('12/16 | loading strength..')
    # load_strength(json_skill_tables[0])
    # print('loaded')
    # print('13/16 | loading strength_junc..')
    # load_strength_junc(strength_junc)
    # print('loaded')
    # print('14/16 | loading course_junc..')
    # load_course_junc(course_junc)
    # print('loaded')
    # print('15/16 | loading course_info..')
    # load_course_info(course_info)
    # print('loaded')
    print('16/16 | loading sparta_day_performance..')
    load_sparta_day_performance(sparta_day_performance1)
    print('loaded')
#
clean_and_load(extracted)

