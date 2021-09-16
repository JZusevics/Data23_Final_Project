import pandas as pd


def sparta_day_extract(talent_txt):
    applicant_day_date = talent_txt['applicant_day_date'].unique()
    applicant_day_date = pd.DataFrame(applicant_day_date)
    applicant_day_date['applicant_day_date_id'] = applicant_day_date.index
    applicant_day_date = applicant_day_date.rename(columns={0: 'applicant_day_date'})
    applicant_day_date = applicant_day_date[['applicant_day_date_id', 'applicant_day_date']]
    talent_txt = talent_txt.merge(applicant_day_date, on='applicant_day_date', how='left')
    talent_txt.pop('applicant_day_date')
    test_location = talent_txt['location'].unique()
    test_location = pd.DataFrame(test_location)
    test_location['location_id'] = test_location.index
    test_location = test_location.rename(columns={0: 'location'})
    test_location = test_location[['location_id', 'location']]
    talent_txt = talent_txt.merge(test_location, on='location', how='left')
    talent_txt.pop('location')
    sparta_day = talent_txt[['applicant_day_date_id', 'location_id']]
    sparta_day = sparta_day.groupby(['applicant_day_date_id', 'location_id']).size().reset_index()
    sparta_day['day_id'] = sparta_day.index
    sparta_day = sparta_day[['day_id', 'applicant_day_date_id', 'location_id']]
    talent_txt = talent_txt.merge(sparta_day, on=['applicant_day_date_id', 'location_id'], how='left')
    talent_txt.pop('applicant_day_date_id')
    talent_txt.pop('location_id')
    return sparta_day, applicant_day_date, test_location, talent_txt


# def create_sparta_day_performance(talent_txt, talent_json):
#
#     sparta_day, applicant_day_date, test_location, talent_txt = sparta_day_extract(talent_txt)
#
#     json_txt_joined = pd.merge(talent_json, talent_txt, on=['candidate_name'], how='outer')
#
#     sparta_day_performance = json_txt_joined.loc[:, ['candidate_id', 'day_id', 'psychometrics_score',
#                                                    'presentation_score', 'financial_support_self', 'pass',
#                                                    'course_interest', 'geo_flex', 'self_development']]
#     sparta_day_performance.rename(columns={'psychometrics_score': 'psychometric_score'}, inplace=True)
#     return sparta_day_performance


def create_sparta_day_performance(talent_txt, talent_json):

    sparta_day, applicant_day_date, test_location, talent_txt = sparta_day_extract(talent_txt)

    applicant_day_date.rename(columns={'applicant_day_date_id': 'day_id'}, inplace=True)
    added_date = pd.merge(talent_txt, applicant_day_date, on=['day_id'], how='outer')

    json_txt_joined = pd.merge(added_date, talent_json, on=['candidate_name', 'applicant_day_date'], how='outer')
    sparta_day_performance = json_txt_joined.loc[:, ['candidate_id', 'day_id', 'psychometrics_score',
                                                       'presentation_score', 'financial_support_self', 'pass',
                                                       'course_interest', 'geo_flex', 'self_development']]
    sparta_day_performance.rename(columns={'psychometrics_score': 'psychometric_score'}, inplace=True)
    return sparta_day_performance

# talent_txt_copy = talent_txt.loc[:, :]
