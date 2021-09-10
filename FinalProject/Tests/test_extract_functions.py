import unittest
import Data23_Final_Project.FinalProject.Apps.extract_academy as ea
import Data23_Final_Project.FinalProject.Apps.extract_txt as et
import Data23_Final_Project.FinalProject.Apps.extract_json as ej
import Data23_Final_Project.FinalProject.Apps.extract_csv as ec
import pandas as pd


class ExtractionTests(unittest.TestCase):

    extracted_csv = ea.extract_academy_csv()
    extracted_txt = et.extract_txt('Talent/Sparta Day 26 September 2019.txt')
    extracted_json = ej.extract_json('Talent/13467.json', {})
    extracted_talent_csv = ec.extract_csv('Talent/April2019Applicants.csv')

    # test to check if academy csv files are extracted correctly
    def test_a_academy_csv(self):
        self.assertEqual(type(self.extracted_csv), list)
        self.assertEqual(type(self.extracted_csv[0][1]), pd.DataFrame)
        self.assertEqual(self.extracted_csv[3][0], 'Academy/Business_23_2019-05-20.csv')
        self.assertEqual(len(self.extracted_csv[0][1].columns), 50)
        self.assertEqual(len(self.extracted_csv[23][1].columns), 62)
        self.assertEqual(self.extracted_csv[23][0], 'Academy/Engineering_17_2019-02-18.csv')
        self.assertEqual(len(self.extracted_csv[0][1]), 8)

    # test to check if txt files are extracted correctly
    def test_b_extract_txt(self):
        self.assertEqual(type(self.extracted_txt), pd.DataFrame)
        self.assertEqual(len(self.extracted_txt.columns), 6)
        self.assertEqual(list(self.extracted_txt.columns), ['First Name', 'Last Name', 'Psychometrics Score',
                                                            'Presentation Score', 'Date', 'Location'])
        self.assertEqual(len(self.extracted_txt), 31)

    # test to check if json files are extracted correctly
    def test_c_extract_json(self):
        self.assertEqual(type(self.extracted_json), dict)
        self.assertEqual(list(self.extracted_json.keys()), ['Latisha Ibel 03/04/2019'])
        self.assertEqual(type(self.extracted_json['Latisha Ibel 03/04/2019']), dict)
        self.assertEqual(list(self.extracted_json['Latisha Ibel 03/04/2019'].keys()),
                         ['name', 'date', 'tech_self_score', 'strengths', 'weaknesses', 'self_development',
                          'geo_flex', 'financial_support_self', 'result', 'course_interest'])
        self.assertEqual(self.extracted_json['Latisha Ibel 03/04/2019']['strengths'], ["Passionate", "Determined"])

    # def test_d_extract_csv(self):

