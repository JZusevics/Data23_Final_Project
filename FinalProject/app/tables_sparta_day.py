import pandas as pd
def sparta_day_extract(talent_txt):

    applicant_day_date = talent_txt['applicant_day_date'].unique()
    applicant_day_date = pd.DataFrame(applicant_day_date)
    applicant_day_date['applicant_day_date_id'] = applicant_day_date.index
    applicant_day_date = applicant_day_date.rename(columns={0:'applicant_day_date'})
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
    talent_txt.pop('applicant_day_date_id')
    talent_txt.pop('location_id')
    return sparta_day, applicant_day_date, test_location, talent_txt
