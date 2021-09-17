import unittest
from datetime import datetime

from FinalProject.app.cleaning_functions.talent_json_cleaning.junction_table_creator import *
from FinalProject.app.cleaning_functions.talent_json_cleaning.json_cleaning_functions import *
from FinalProject.app.cleaning_functions.talent_json_cleaning.df_transform import *
from FinalProject.app.cleaning_functions.talent_json_cleaning.id_extract import *

class CleanJsonTests(unittest.TestCase):
    test_json_dict = {"Valle Humby 21/08/2019":{"name": "Valle Humby", "date": "21/08/2019",
                                               "tech_self_score": {"Python": 2, "C#": 1, "Ruby": 2, "SPSS": 5, "JavaScript": 2},
                                               "strengths": ["Competitive"], "weaknesses": ["Perfectionist", "Intolerant"],
                                               "self_development": "Yes", "geo_flex": "Yes", "financial_support_self": "Yes", "result": "Pass",
                                               "course_interest": "Engineering"},
                      "Phillis Wabey 06/08/2019":{"name": "Phillis Wabey", "date": "06/08/2019", "tech_self_score": {"Python": 1, "C#": 3, "R": 2, "SPSS": 2},
                                                  "strengths": ["Problem Solving"], "weaknesses": ["Overbearing", "Impatient"],
                                                  "self_development": "Yes", "geo_flex": "Yes", "financial_support_self": "Yes",
                                                  "result": "Pass", "course_interest": "Data"}}
    date_format = "%d-%m-%Y"
    yes_no_keys = ['self_development', 'financial_support_self', 'geo_flex']
    test_json_keys = test_json_dict.keys()
    removed_keys_json = key_remover(test_json_keys, test_json_dict)

    def test_a_key_remover(self):
        self.assertEqual(len(self.removed_keys_json), 2)
        self.assertEqual(len(self.removed_keys_json[1].keys()), 7)

    bool_fix_test = bool_fix(test_json_keys, test_json_dict, yes_no_keys)
    def test_b_skill_id(self):
        self.assertEqual(self.bool_fix_test["Valle Humby 21/08/2019"]["self_development"], True)
        self.assertEqual(self.bool_fix_test["Phillis Wabey 06/08/2019"]["financial_support_self"], True)

    results_fix_test = results_fix(test_json_keys, test_json_dict)
    print (results_fix_test)
    def test_c_results_fix(self):
        self.assertEqual(self.results_fix_test["Valle Humby 21/08/2019"]['pass'], True)
        self.assertEqual(self.results_fix_test["Phillis Wabey 06/08/2019"]['pass'], True)

    tech_skill_df_test = tech_candidate_id_creator(test_json_keys, test_json_dict, 'tech_self_score')
    def test_d_tech_candidate_id_creator(self):
        self.assertEqual(list(self.tech_skill_df_test.columns), ['id', 'skill', 'score'])

    strength_df_test = strengths_candidate_id_creator(test_json_keys, test_json_dict, 'strengths')
    def test_e_strengths_candidate_id_creator(self):
        self.assertEqual(list(self.strength_df_test.columns), ['id', 'skill'])

    test_json_dict_skill = {"Valle Humby 21/08/2019": {"name": "Valle Humby", "date": "21/08/2019",
                                                 "tech_self_score": {"Python": 2, "C#": 1, "Ruby": 2, "SPSS": 5,
                                                                     "JavaScript": 2},
                                                 "strengths": ["Competitive"],
                                                 "weaknesses": ["Perfectionist", "Intolerant"],
                                                 "self_development": "Yes", "geo_flex": "Yes",
                                                 "financial_support_self": "Yes", "result": "Pass",
                                                 "course_interest": "Engineering"},
                      "Phillis Wabey 06/08/2019": {"name": "Phillis Wabey", "date": "06/08/2019",
                                                   "tech_self_score": {"Python": 1, "C#": 3, "R": 2, "SPSS": 2},
                                                   "strengths": ["Problem Solving"],
                                                   "weaknesses": ["Overbearing", "Impatient"],
                                                   "self_development": "Yes", "geo_flex": "Yes",
                                                   "financial_support_self": "Yes",
                                                   "result": "Pass", "course_interest": "Data"}}
    test_json_keys_skill = test_json_dict_skill.keys()
    tech_skill_id_test = tech_skill_id_generator(test_json_keys, 'tech_self_score', test_json_dict_skill)
    def test_f_tech_skill_id_generator(self):
          self.assertEqual(self.tech_skill_id_test[2], 'C#')
          self.assertEqual(self.tech_skill_id_test[6], 'R')
          self.assertEqual(self.tech_skill_id_test[5], 'JavaScript')

    skill_strength_id_generator_test = skill_id_generator(test_json_keys, 'strengths', test_json_dict_skill)
    skill_weakness_id_generator_test = skill_id_generator(test_json_keys, 'weaknesses', test_json_dict_skill)
    def test_g_skill_id_generator(self):
          self.assertEqual(self.skill_strength_id_generator_test[2], 'Problem Solving')
          self.assertEqual(self.skill_strength_id_generator_test[1], 'Competitive')
          self.assertEqual(self.skill_weakness_id_generator_test[1], 'Perfectionist')
          self.assertEqual(self.skill_weakness_id_generator_test[4], 'Impatient')
