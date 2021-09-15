import pandas as pd


def cand_id_gen_txt(scores: pd.DataFrame):
    scores["candidate_id_str"] = scores["first_name"]+" "+scores["last_name"] + " " + scores["date"].map(str)
    temp = scores[~scores["middle_name"].isnull()]
    scores.loc[~scores["middle_name"].isna(), ["candidate_id_str"]] = temp["first_name"] + " " + temp["middle_name"] + " " + temp["last_name"] + " " + temp["date"].map(str)
    scores['candidate_name'] = scores['candidate_id_str'].map(lambda x: x[:-11])
    scores = scores[["candidate_id_str", "candidate_name", "first_name", "middle_name", "last_name", "psychometrics_score", "presentation_score", "date", "location"]]
    scores.rename(columns={'date': 'applicant_day_date'}, inplace=True)
    return scores

