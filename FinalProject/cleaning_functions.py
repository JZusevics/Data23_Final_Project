import json
import datetime
import numpy
import pandas as pd
import os
import csv


def json_cleaning(candidate_json, candidate_json_keys, date_format, yes_no_keys):
    def internal_id_append(json_keys, json):
        """
        This Creates an internal id for creation of data frame, so that all data can be referenced and have a new id assigned
        :param json_keys: Keys that point to each json in the json file
        :param candidate_json: Json file of candidate date
        :return: Json files updated with a candidate key selection
        """
        candidate_id = 0
        for name in list(json_keys):
            json[name]['internal_id'] = candidate_id
            candidate_id += 1
        return json


    def date_test(name_dates, format, candidate_json):
        """
        Test that the dates are in a datetime format, then rearranges them to match our sql format
        Tests that dates are
        :param name_dates: Keys for iterating through the json file
        :param format: The date format the original dates should be in
        :param candidate_json: The json of all of the candidate date
        :return: candidate-json with and updated date format
        """
        for candidate in name_dates:
            # replaces / characters with - for sql
            date = candidate_json[candidate]['date']
            date = date.replace('/', '-')
            # try and except loop to stop breaks when key is not found in json
            try:
                date = datetime.datetime.strptime(date, format).strftime("%Y-%m-%d")
                candidate_json[candidate]['date'] = date
                candidate_json[candidate]['applicant_day_date'] = candidate_json[candidate]['date']
                del candidate_json[candidate]['date']
            except ValueError:
                # fixes standard error of too many dashes
                 date = date.replace('-', '', 1)
                 try:
                     date = datetime.datetime.strptime(date, format).strftime("%Y-%m-%d")
                     candidate_json[candidate]['date'] = date
                     candidate_json[candidate]['applicant_day_date'] = candidate_json[candidate]['date']
                     del candidate_json[candidate]['date']
                 except ValueError:
                    print("Value error date ", date, " not in correct format")

        return candidate_json


    def bool_fix(name_dates, candidate_json, yes_no_key):
        """
        Test that bool the three boolean key date pairs of financial_support_self, geo_flex and self_development are true
        :param name_dates: Keys for iterating through the json file
        :param candidate_json: the json of all of the candidate date
        :param yes_no_key: List of three keys we are testing
        :return:
        """
        for candidate in name_dates:
                for key in yes_no_keys:
                    test = str(candidate_json[candidate][key].strip())
                    if test == 'Yes' or test == 'yes' or test == 'Y' or test == 'y':
                        candidate_json[candidate][key] = True
                    elif test == 'No' or test == 'no' or test == 'N' or test == 'n':
                        candidate_json[candidate][key] = False
                    else:
                        # returns incorrect data for error exploration
                        print(test)
        return candidate_json


    def results_fix(name_dates, candidate_json):
        """
        Changes the results key to pass and converts pass or fail to true or false to enable boolean or bit logic
        :param name_dates:
        :param candidate_json:
        :return: Updated candidate_json
        """
        for candidate in name_dates:
            test = str(candidate_json[candidate]['result'])
            candidate_json[candidate]['pass'] = candidate_json[candidate]['result']
            del candidate_json[candidate]['result']
            if test == 'Pass':
                candidate_json[candidate]['pass'] = True
            elif test == 'Fail':
                candidate_json[candidate]['pass'] = False
            else:
                # returns incorrect data for error exploration
                print(test)
        return candidate_json


    def name_strip(name_dates ,candidate_json):
        """
        Strips white space off of names, might not be nesaccary
        :param name_dates:
        :param candidate_json:
        :return:
        """
        for candidate in name_dates:
            candidate_json[candidate]['name'] = str(candidate_json[candidate]['name']).strip().lower().title()
            # code commented out can be used to check for incorrect name formats
            # if str(candidate_json[candidate]['name']).strip().lower().title().count(' ') > 1:
            # print(str(candidate_json[candidate]['name']).strip().lower().title())
        return candidate_json

    candidate_json = internal_id_append(candidate_json_keys, candidate_json)
    candidate_json = name_strip(candidate_json_keys, candidate_json)
    candidate_json = date_test(candidate_json_keys, date_format, candidate_json)
    candidate_json = bool_fix(candidate_json_keys, candidate_json, yes_no_keys)
    candidate_json = results_fix(candidate_json_keys, candidate_json)
    return candidate_json

