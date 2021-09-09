import unittest
import Data23_Final_Project.FinalProject.App.extract_academy as ea
import Data23_Final_Project.FinalProject.App.extract_txt as et
import pandas as pd


class ExtractionTests(unittest.TestCase):

    extracted_csv = ea.extract_academy_csv()
    extracted_txt = et.extract_txt('Talent/Sparta Day 26 September 2019.txt')

    # test to check if academy csv files are extracted correctly
    def test_a_academy_csv(self):
        self.assertEqual(type(self.extracted_csv), list)
        self.assertEqual(type(self.extracted_csv[0][1]), pd.DataFrame)
        self.assertEqual(self.extracted_csv[3][0], 'Academy/Business_23_2019-05-20.csv')
        self.assertEqual(len(self.extracted_csv[0][1].columns), 50)

    # test to check if txt files are extracted correctly
    def test_b_extract_txt(self):
        self.assertEqual(type(self.extracted_txt), pd.DataFrame)
        self.assertEqual(len(self.extracted_txt.columns), 6)
        self.assertEqual(list(self.extracted_txt.columns), ['First Name', 'Last Name', 'Psychometrics Score',
                                                            'Presentation Score', 'Date', 'Location'])
