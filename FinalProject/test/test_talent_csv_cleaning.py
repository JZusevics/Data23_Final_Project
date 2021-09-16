import unittest

from Data23_Final_Project.FinalProject.app.cleaning_functions.id_into_txt import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_csv_cleaning.clean_talent_csv import *


class CleaningCsvTests(unittest.TestCase):
    dates_test = {'invited_date': [10.0, np.nan, 2.0, 5.0, 11.0],
                  'month': ['April 2019', np.nan, 'June 2019', 'January 2019', 'April 2020']}
    dates_df = pd.DataFrame(dates_test)
    clean_dates = talent_csv_invite_date(dates_df)

    def test_a_talent_csv_date(self):
        self.assertEqual(self.clean_dates.iloc[0, 0], datetime.strptime('2019-04-10', '%Y-%m-%d').date())
        self.assertTrue(pd.isnull(self.clean_dates.iloc[1, 0]))
        self.assertEqual(self.clean_dates.iloc[2, 0], datetime.strptime('2019-06-02', '%Y-%m-%d').date())
        self.assertEqual(self.clean_dates.iloc[3, 0], datetime.strptime('2019-01-05', '%Y-%m-%d').date())
        self.assertEqual(self.clean_dates.iloc[4, 0], datetime.strptime('2020-04-11', '%Y-%m-%d').date())

    dob_test = {'dob': ['05/12/1992', np.nan, '12/01/1995', '24/04/1993', '03/10/1994', np.nan]}
    dob_df = pd.DataFrame(dob_test)
    clean_dob = talent_csv_dob(dob_df)

    def test_b_talent_csv_dob(self):
        self.assertEqual(self.clean_dob.iloc[0, 0], datetime.strptime('1992-12-05', '%Y-%m-%d').date())
        self.assertTrue(pd.isnull(self.clean_dob.iloc[1, 0]))
        self.assertEqual(self.clean_dob.iloc[2, 0], datetime.strptime('1995-01-12', '%Y-%m-%d').date())
        self.assertEqual(self.clean_dob.iloc[3, 0], datetime.strptime('1993-04-24', '%Y-%m-%d').date())
        self.assertTrue(self.clean_dob.iloc[4, 0], datetime.strptime('1994-10-03', '%Y-%m-%d').date())
        self.assertTrue(pd.isnull(self.clean_dob.iloc[5, 0]))

    phone_test = {'phone_number': ['+44 346 234-7524', np.nan, '+44 (343) 436 4352', '+44-234-234-7632',
                                   '+44 (954) 354-3242', np.nan]}
    phone_df = pd.DataFrame(phone_test)
    clean_phone = talent_csv_phone(phone_df)

    def test_c_talent_csv_phone(self):
        self.assertEqual(self.clean_phone.iloc[0, 0], '+443462347524')
        self.assertTrue(pd.isnull(self.clean_phone.iloc[1, 0]))
        self.assertEqual(self.clean_phone.iloc[2, 0], '+443434364352')
        self.assertEqual(self.clean_phone.iloc[3, 0], '+442342347632')
        self.assertTrue(self.clean_phone.iloc[4, 0], '+449543453242')
        self.assertTrue(pd.isnull(self.clean_phone.iloc[5, 0]))

    column_names_test = {"email": ["abc@aol.com", "click@google.jp"],
                         "uni": ["University of Warwick", "Keele University"],
                         "id": [4, '29'],
                         "invited_by": ["Jennifer Holden", np.nan]}
    columns_df = pd.DataFrame(column_names_test)
    cleaned_columns = talent_csv_column_names_erd(columns_df)

    def test_d_talent_csv_column_names_erd(self):
        self.assertEqual(self.cleaned_columns["applicant_day_trainee_id"].dtype, np.int32)
        self.assertEqual(type(self.cleaned_columns.iloc[0, 0]), str)
        self.assertEqual(type(self.cleaned_columns.iloc[0, 1]), str)
        self.assertEqual(type(self.cleaned_columns.iloc[1, 2]), np.int32)
        self.assertEqual(type(self.cleaned_columns.iloc[0, 3]), str)
        self.assertTrue(pd.isnull(self.cleaned_columns.iloc[1, 3]))
        self.assertEqual(type(self.cleaned_columns.iloc[1, 3]), float)

    id_gen_test = {'name': ['Callumn Robinson', 'Marco De Silva', 'Jessica Alves', 'Danny O Sulivan',
                            'Bob Andy Roberts', "Lucy Dell 'Otto", "Von Schule Potro"]}
    id_gen_df = pd.DataFrame(id_gen_test)
    id_generated = talent_csv_id_gen(id_gen_df)

    def test_e_talent_csv_id_gen(self):
        self.assertEqual(len(self.id_generated.columns), 2)
        self.assertEqual(list(self.id_generated.columns), ["name", "candidate_id"])
        self.assertEqual(self.id_generated.iloc[0, 1], 1)
        self.assertEqual(len(self.id_generated[self.id_generated.duplicated('candidate_id', keep=False)]), 0)
