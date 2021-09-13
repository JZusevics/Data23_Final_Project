import json
import datetime
f = open('data.json')
candidate_json = json.load(f)

#print(candidate_json)


name_dates = candidate_json.keys()
date_format = "%d-%m-%Y"


def date_test(name_dates, format, candidate_json):
    for candidate in name_dates:
         date = candidate_json[candidate]['date']
         date = date.replace('/', '-')
         try:
             datetime.datetime.strptime(date, format)
             candidate_json[candidate]['date'] = date
         except ValueError:
             # fixes standard error of too many dases
             date = date.replace('-', '', 1)
             try:
                 datetime.datetime.strptime(date, format)
                 candidate_json[candidate]['date'] = date
             except ValueError:
                print("Value error date ", date, " not in correct format")
    return candidate_json

yes_no_keys = ['self_development', 'financial_support_self', 'geo_flex']
# test that bools are of the right values


def bool_fix(name_dates, candidate_json):
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


def results_fix(name_date, candidate_json):
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
    for candidate in name_dates:
        candidate_json[candidate]['name'] = str(candidate_json[candidate]['name']).strip().lower().title()
        # code commented out can be used to check for incorrect name formats
        #if str(candidate_json[candidate]['name']).strip().lower().title().count(' ') > 1:
         #   print(str(candidate_json[candidate]['name']).strip().lower().title())
    return name_dates


def skill_id_generator(name_dates, skill):
    list_strengths = []
    for candidate in name_dates:
        strengths = candidate_json[candidate][skill]
        for strength in strengths:
            if strength not in list_strengths:
                list_strengths.append(strength)
        i = 1
    strengths_id = {}
    for strength in list_strengths:
        strengths_id.update({strength: i})
        i = i+1
    for candidate in name_dates:
        strengths = candidate_json[candidate][skill]
        for i, strength in enumerate(strengths):
            id = strengths_id[strength]
            candidate_json[candidate][skill][i] = id
    return strengths_id


def tech_skill_id_generator(name_dates, skill):
    list_strengths = []
    for candidate in name_dates:
        try:
            strengths = candidate_json[candidate][skill]
            for strength in strengths:
                if strength not in list_strengths:
                    list_strengths.append(strength)
        except KeyError:
            pass
    i = 1
    strengths_id = {}
    for strength in list_strengths:
        strengths_id.update({strength: i})
        i = i+1
    for candidate in name_dates:
        try:
            strengths = candidate_json[candidate][skill]
            for strength in list(strengths):
                candidate_json[candidate][skill][strengths_id[strength]] = candidate_json[candidate][skill][strength]
                del candidate_json[candidate][skill][strength]
        except KeyError:
           pass
    return strengths_id

name_strip(name_dates, candidate_json)
candidate_json = date_test(name_dates, date_format, candidate_json)
strengths_id = skill_id_generator(name_dates, 'strengths')
weakness_id = skill_id_generator(name_dates, 'weaknesses')
tech_skill_id = tech_skill_id_generator(name_dates, 'tech_self_score')
candidate_json = bool_fix(name_dates, candidate_json)
candidate_json = results_fix(name_dates, candidate_json)

with open('data_clean.json', 'w') as fp:
    json.dump(candidate_json, fp, sort_keys=True, indent=4)