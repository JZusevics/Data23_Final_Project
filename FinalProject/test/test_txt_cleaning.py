import unittest
import pandas as pd
import numpy as np
from Data23_Final_Project.FinalProject.app.cleaning_functions.split_names import *
from Data23_Final_Project.FinalProject.app.cleaning_functions.generate_id import *


class CleaningTxtTests(unittest.TestCase):

    names_test = {'name': [
        'Callumn Robinson',
        'Marco De Silva',
        'Jessica Alves',
        'Danny O Sulivan',
        'Bob Andy Roberts',
        "Lucy Dell 'Otto"
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
