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

    inviter = talent['invited_by_name'].dropna().unique()
    inviter = pd.DataFrame(inviter)
    inviter['inviter_id'] = inviter.index
    inviter = inviter.rename(columns={0:'invited_by_name'})
    inviter = inviter[['inviter_id', 'invited_by_name']]
    talent = talent.merge(inviter, on='invited_by_name', how='left')
    talent.pop('invited_by_name')

    trainer = academy_performance['trainer'].dropna().unique()
    trainer = pd.DataFrame(trainer)
    trainer = trainer.rename(columns={0: 'trainer'})
    trainer['trainer_id'] = trainer.index
    academy_performance = academy_performance.merge(trainer, on='trainer', how='left')
    trainer = trainer.rename(columns={'trainer': 'trainer_name'})
    trainer = trainer[['trainer_id', 'trainer_name']]
    academy_performance.pop('trainer')

    return inviter, talent, trainer, academy_performance
