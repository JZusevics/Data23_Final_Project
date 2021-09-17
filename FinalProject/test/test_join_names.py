import unittest
import numpy as np
import pandas as pd

from FinalProject.app.cleaning_functions.join_names_csv import full_name
from FinalProject.app.cleaning_functions.id_into_txt import candidate_id_into_txt




class JoinNameTests(unittest.TestCase):
    names_test = {'first_name': ['Callum', 'Marco', 'Jessica', 'Danny', 'Bob', "Lucy", "Vonschule"],
                  'middle_name': [np.nan, np.nan, np.nan, np.nan, 'Andy', np.nan, np.nan],
                  'last_name': ['Robinson', 'De Silva', 'Alves', 'O Sulivan', 'Roberts', "Dell'Otto", 'Potro']}
    test_df = pd.DataFrame(names_test)
    joined_name = full_name(test_df)

    def test_a_join_names_csv(self):
        self.assertEqual(len(self.joined_name.columns), 4)
        self.assertEqual(list(self.joined_name.columns), ['first_name', 'middle_name', 'last_name', 'candidate_name'])
        self.assertEqual(self.joined_name.iloc[0, 3], 'Callum Robinson')
        self.assertEqual(self.joined_name.iloc[1, 3], 'Marco De Silva')
        self.assertEqual(self.joined_name.iloc[4, 3], 'Bob Andy Roberts')

    join_df_txt = {'candidate_name': ['Callum', 'Marco', 'Jessica', 'Danny', 'Bob', "Lucy", "Vonschule"],
                   'applicant_day_date': ['20/07', '23/06', '28/08', '22/04', '08/07', '13/09', '31/12'],
                   'candidate_id_str': ['Callum 20/07', 'Marco 23/06', 'Jessica 28/08', 'Danny 22/04', 'Bob 08/07',
                                        "Lucy 13/09", "Vonschule 31/12"],
                   'score': [80, 75, 90, 85, 60, 95, 62],
                   'age': [19, 18, 23, 19, 30, 24, 24]}
    test_txt_df = pd.DataFrame(join_df_txt)
    join_table_csv = {'candidate_name': ['Callum', 'Danny', 'Bob', "Lucy", "Vonschule", "John", "Jericho"],
                      'applicant_day_date': ['20/07', '22/04', '08/07', '13/09', '31/12', '05/05', '03/08'],
                      'candidate_id': [1, 4, 5, 6, 7, 8, 9],
                      'second_score': [80, 85, 60, 95, 62, 93, 80]}
    test_csv_df = pd.DataFrame(join_table_csv)
    join_table = candidate_id_into_txt(test_csv_df, test_txt_df)
    def test_b_id_into_txt(self):
        self.assertEqual(len(self.join_table.columns), 6)
        self.assertEqual(self.join_table.iloc[0, 2], 'Callum 20/07')
        self.assertEqual(list(self.join_table.columns)[:6], ['candidate_name', 'applicant_day_date',
                                                                'candidate_id_str', 'score', 'age', 'candidate_id'])
        self.assertEqual(list(self.join_table.iloc[3, :]), ["Danny", "22/04", "Danny 22/04", 85, 19 ,4.0])