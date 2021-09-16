import unittest
from datetime import datetime

from Data23_Final_Project.FinalProject.app.cleaning_functions.split_names import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_txt_cleaning.generate_id import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.talent_txt_cleaning.remove_academy import *


class CleaningTxtTests(unittest.TestCase):
    names_test = {'name': [
        'Callumn Robinson',
        'Marco De Silva',
        'Jessica Alves',
        'Danny O Sulivan',
        'Bob Andy Roberts',
        "Lucy Dell 'Otto",
        "Von Schule Potro"
    ]}
    test_df = pd.DataFrame(names_test)
    split = split_names(test_df)

    def test_a_split_names(self):
        self.assertEqual(len(self.split.columns), 3)
        self.assertEqual(list(self.split.columns), ['first_name', 'middle_name', 'last_name'])
        self.assertEqual(self.split.iloc[4, 1], 'Andy')
        self.assertEqual(self.split.iloc[1, 2], 'De Silva')
        self.assertEqual(self.split.iloc[3, 2], 'O Sulivan')
        self.assertTrue(np.isnan(self.split.iloc[3, 1]))
        self.assertEqual(self.split.iloc[4, 1], 'Andy')
        self.assertEqual(self.split.iloc[5, 2], "Dell'Otto")
        self.assertEqual(list(self.split.iloc[6, :]), ["Vonschule", np.nan, "Potro"])

    cand_id_test = {'first_name': ['Callumn', 'Marco', 'Jessica', 'Danny', 'Bob', "Lucy", "Vonschule"],
                    'middle_name': [np.nan, np.nan, np.nan, np.nan, 'Andy', np.nan, np.nan],
                    'last_name': ['Robinson', 'De Silva', 'Alves', 'O Sulivan', 'Roberts', "Dell'Otto", "Potro"],
                    'date': [
                        datetime.strptime('2019-2-18', '%Y-%m-%d').date(),
                        datetime.strptime('2019-1-8', '%Y-%m-%d').date(),
                        datetime.strptime('2019-8-1', '%Y-%m-%d').date(),
                        datetime.strptime('2019-12-12', '%Y-%m-%d').date(),
                        datetime.strptime('2019-5-28', '%Y-%m-%d').date(),
                        datetime.strptime('2019-1-4', '%Y-%m-%d').date(),
                        datetime.strptime('2019-11-11', '%Y-%m-%d').date()],
                    'psychometrics_score': np.zeros(7),
                    'presentation_score': np.zeros(7),
                    'location': np.zeros(7)
                    }
    gen_id_df = pd.DataFrame(cand_id_test)
    generated_id = cand_id_gen_txt(gen_id_df)

    def test_b_generate_id(self):
        self.assertEqual(len(self.generated_id.columns), 9)
        self.assertEqual(list(self.generated_id.columns),
                         ["candidate_id_str", "candidate_name", "first_name", "middle_name",
                          "last_name", "psychometrics_score", "presentation_score",
                          "applicant_day_date", "location"])
        self.assertEqual(self.generated_id.iloc[0, 0], 'Callumn Robinson 2019-02-18')
        self.assertEqual(self.generated_id.iloc[4, 1], 'Bob Andy Roberts')
        self.assertEqual(self.generated_id.iloc[5, 0], "Lucy Dell'Otto 2019-01-04")
        self.assertEqual(self.generated_id.iloc[1, 1], 'Marco De Silva')

    location_test = {'location': [
        'London Academy',
        'Manchester Academy',
        'Birmingham',
        'Birmingham Academy',
        'Lincoln',
        'Brighton',
        'Liverpool Academy'
    ]}
    loc_test_df = pd.DataFrame(location_test)
    removed_academy = clean_location(loc_test_df)

    def test_c_remove_academy(self):
        self.assertEqual(self.removed_academy.iloc[0, 0], 'London')
        self.assertEqual(self.removed_academy.iloc[1, 0], 'Manchester')
        self.assertEqual(self.removed_academy.iloc[2, 0], 'Birmingham')
        self.assertEqual(self.removed_academy.iloc[5, 0], 'Brighton')
        self.assertEqual(self.removed_academy.iloc[6, 0], 'Liverpool')
