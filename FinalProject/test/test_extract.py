import unittest
from Data23_Final_Project.FinalProject.app.extract_functions.extract_all import *


class ExtractionTests(unittest.TestCase):

    extracted_csv = extract_academy_csv()

    # test to check if academy csv files are extracted correctly
    def test_a_academy_csv(self):
        self.assertEqual(type(self.extracted_csv), list)
        self.assertEqual(type(self.extracted_csv[0][1]), pd.DataFrame)
        self.assertEqual(self.extracted_csv[3][0], 'Academy/Business_23_2019-05-20.csv')
        self.assertEqual(len(self.extracted_csv[0][1].columns), 50)
        self.assertEqual(len(self.extracted_csv[23][1].columns), 62)
        self.assertEqual(self.extracted_csv[23][0], 'Academy/Engineering_17_2019-02-18.csv')
        self.assertEqual(len(self.extracted_csv[0][1]), 8)

    extracted_txt = extract_txt('Talent/Sparta Day 26 September 2019.txt')

    # test to check if txt files are extracted correctly
    def test_b_extract_txt(self):
        self.assertEqual(type(self.extracted_txt), pd.DataFrame)
        self.assertEqual(len(self.extracted_txt.columns), 5)
        self.assertEqual(list(self.extracted_txt.columns), ['name', 'psychometrics_score',
                                                            'presentation_score', 'date', 'location'])
        self.assertEqual(len(self.extracted_txt), 31)

    extracted_json = extract_json('Talent/13467.json', {})

    # test to check if json files are extracted correctly
    def test_c_extract_json(self):
        self.assertEqual(type(self.extracted_json), dict)
        self.assertEqual(list(self.extracted_json.keys()), ['Latisha Ibel 03/04/2019'])
        self.assertEqual(type(self.extracted_json['Latisha Ibel 03/04/2019']), dict)
        self.assertEqual(list(self.extracted_json['Latisha Ibel 03/04/2019'].keys()),
                         ['name', 'date', 'tech_self_score', 'strengths', 'weaknesses', 'self_development',
                          'geo_flex', 'financial_support_self', 'result', 'course_interest'])
        self.assertEqual(self.extracted_json['Latisha Ibel 03/04/2019']['strengths'], ["Passionate", "Determined"])

    extracted_talent_csv = extract_csv('Talent/April2019Applicants.csv')
    extracted_talent_csv_2 = extract_csv('Talent/Feb2019Applicants.csv')

    # test to check if talent csv files are extracted correctly
    def test_d_extract_csv(self):
        self.assertEqual(type(self.extracted_talent_csv), pd.DataFrame)
        self.assertEqual(len(self.extracted_talent_csv), 379)
        self.assertEqual(len(self.extracted_talent_csv.columns), 14)
        self.assertEqual(list(self.extracted_talent_csv.columns), ['id', 'name', 'gender', 'dob', 'email', 'city',
                                                                   'address', 'postcode', 'phone_number', 'uni',
                                                                   'degree', 'invited_date', 'month', 'invited_by'])
        self.assertEqual(len(self.extracted_talent_csv_2), 372)
        self.assertEqual(len(self.extracted_talent_csv_2.columns), 14)

    extracted_all = extract_all()

    # test to check if all files are extracted correctly in one function
    def test_e_extract_all(self):
        self.assertEqual(type(self.extracted_all[0]), list)
        self.assertEqual(type(self.extracted_all[0][0][1]), pd.DataFrame)

        self.assertEqual(type(self.extracted_all[1]), dict)
        self.assertEqual(type(self.extracted_all[1]['Zsa Zsa Rounsefull 16/07/2019']), dict)
        self.assertEqual(len(list(self.extracted_all[1].values())), 3105-32)  # 32 duplicate data

        self.assertEqual(type(self.extracted_all[2]), pd.DataFrame)
        self.assertEqual(len(self.extracted_all[2].columns), 5)
        self.assertEqual(list(self.extracted_all[2].columns), ['name', 'psychometrics_score',
                                                            'presentation_score', 'date', 'location'])

        self.assertEqual(type(self.extracted_all[3]), pd.DataFrame)
        self.assertEqual(len(self.extracted_all[3].columns), 14)
        self.assertEqual(list(self.extracted_all[3].columns), ['id', 'name', 'gender', 'dob', 'email', 'city',
                                                                   'address', 'postcode', 'phone_number', 'uni',
                                                                   'degree', 'invited_date', 'month', 'invited_by'])
