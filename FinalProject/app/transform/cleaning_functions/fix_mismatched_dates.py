import pandas as pd


def join_json_and_csv(talent_json, talent_csv):
    json_txt_joined = pd.merge(talent_json, talent_csv, on=['candidate_name'], how='outer')
    dupe_names = json_txt_joined[json_txt_joined['candidate_name'].duplicated(keep=False)]
    incorrect_dupes = dupe_names[
        dupe_names['applicant_day_date_x'].astype(str) != dupe_names['applicant_day_date_y'].astype(str)]
    return json_txt_joined.drop(index=list(incorrect_dupes.index))


def find_correct_dates(df):
    mismatched_dates = df[~(df['applicant_day_date_x'].astype(str) == df['applicant_day_date_y'].astype(str))]
    wrong_dates = mismatched_dates[~mismatched_dates['applicant_day_date_x'].isna()]
    return wrong_dates.loc[:, ['candidate_name', 'applicant_day_date_y']]


def update_incorrect_dates(talent_json, talent_csv):

    dropped_dupes = join_json_and_csv(talent_json, talent_csv)

    correct_json_dates = find_correct_dates(dropped_dupes)

    matched_dates = dropped_dupes[
        (dropped_dupes['applicant_day_date_x'].astype(str) == dropped_dupes['applicant_day_date_y'].astype(str))]
    original_matched_dates = matched_dates.loc[:, ['candidate_name', 'applicant_day_date_y']]
    updated_dates = pd.concat([correct_json_dates, original_matched_dates]).rename(
        columns={'applicant_day_date_y': 'applicant_day_date'})

    dropped_old_dates = talent_json.drop(columns=['applicant_day_date'])
    return pd.merge(dropped_old_dates, updated_dates, on=['candidate_name'], how='inner')
