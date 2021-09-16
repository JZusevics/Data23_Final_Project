import pandas as pd
def id_generator(academy_csv):
    course_info = academy_csv.groupby(['course_name', 'course_number', 'course_start_date']).size().reset_index()
    course_info['course_id'] = course_info.index
    course_info = course_info[['course_id','course_name', 'course_number', 'course_start_date']]
    course_junc = pd.merge(course_info, academy_csv, on = ['course_name', 'course_number', 'course_start_date'], how='inner', indicator=False)
    course_junc = course_junc[['candidate_id', 'course_id']]
    academy_csv.pop('course_name')
    academy_csv.pop('course_number')
    academy_csv.pop('course_start_date')
    return academy_csv, course_junc, course_info


def trainer_inviter_table_creator(academy_performance, talent):
    inviter = talent['invited_by']
    inviter['invited_by_id'] = inviter.index
    inter.rename(columnse={'invited_by':})