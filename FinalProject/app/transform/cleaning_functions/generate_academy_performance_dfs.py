import pandas as pd
import numpy as np


def generate_candidate_ids_with_performance_scores(academy_csv, talent_txt):
    academy_csv_txt_joined = pd.merge(academy_csv, talent_txt, on=['candidate_name'], how='inner')
    renamed = academy_csv_txt_joined.rename(columns={'candidate_id': 'temp_candidate_id'})
    index = list(academy_csv_txt_joined.columns).index('Analytic_W1')
    renamed.insert(index, 'candidate_id', renamed['temp_candidate_id'])
    return renamed.iloc[:, index:index+61]


def create_academy_performance(academy_csv, talent_txt):
    useful = generate_candidate_ids_with_performance_scores(academy_csv, talent_txt)
    sparta_skills = set()
    for col in useful.columns:
        if col != 'candidate_id':
            dash_index = col.index("_")
            skill = col[:dash_index].lower()
            sparta_skills.add(skill)
    sparta_skills_list = list(sparta_skills)
    sparta_skill_dict = {'sparta_skill_id': list(map(lambda x: x + 1, np.arange(len(sparta_skills_list)))),
                         'skill_name': sparta_skills_list}
    sparta_skill = pd.DataFrame(sparta_skill_dict)

    cand_ids = []
    weeks = []
    skills = []
    scores = []

    for index, row in useful.iterrows():
        for col in row.index:
            if col != 'candidate_id' and not np.isnan(row[col]):
                dash_index = col.index("_")
                skill_id = sparta_skills_list.index(col[:dash_index].lower()) + 1
                week = col[dash_index + 2:]
                cand_ids.append(int(row['candidate_id']))
                weeks.append(week)
                skills.append(int(skill_id))
                scores.append(int(row[col]))

    academy_performance_dict = {'candidate_id': cand_ids, 'week': weeks, 'sparta_skill_id': skills, 'score': scores}
    academy_performance = pd.DataFrame(academy_performance_dict)

    return sparta_skill, academy_performance
