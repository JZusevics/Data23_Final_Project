import pandas as pd
def id_replace_call(json_skill_tables, talent_json_merge):
    strength_junc = id_replace(json_skill_tables[3], talent_json_merge)
    weakness_junc = id_replace(json_skill_tables[4], talent_json_merge)
    tech_self_score = id_replace_skill(json_skill_tables[5], talent_json_merge)
    return(strength_junc, weakness_junc, tech_self_score)

def id_replace(skill_df, large_df):

    skill_df = skill_df.set_index('internal_id').join(large_df.set_index('internal_id'))
    skilL_df = skill_df[['candidate_id', 'skill_id']]
    return skilL_df

def id_replace_skill(skill_df, large_df):
    skill_df = skill_df.set_index('internal_id').join(large_df.set_index('internal_id'))
    skilL_df = skill_df[['candidate_id', 'skill_id', 'score']]
    return skilL_df