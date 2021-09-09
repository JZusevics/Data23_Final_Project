import json
import datetime
f = open('data.json')
candidate_json = json.load(f)

#print(candidate_json)


name_dates = candidate_json.keys()
format = "%d-%m-%Y"
for candidate in name_dates:
     date = candidate_json[candidate]['date']
     date = date.replace('/', '-')
     try:
         datetime.datetime.strptime(date, format)
     except ValueError:
         # fixes standard error of too many dases
         date = date.replace('-', '', 1)
         try:
             datetime.datetime.strptime(date, format)
             candidate_json[candidate]['date'] = date
         except ValueError:
            print("Value error date ", date, " not in correct format")

yes_no_keys = ['self_development', 'financial_support_self', 'geo_flex']
# test that bools are of the right values
for candidate in name_dates:
    for key in yes_no_keys:
        test = str(candidate_json[candidate][key].strip())
        if test == 'Yes' or test == 'yes' or test == 'y' or test =:
            candidate_json[candidate][key] = True
        elif test == 'No':
            candidate_json[candidate][key] = False
        else:
            # returns incorrect data for error exploration
            print(test)

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

with open('data_clean.json', 'w') as fp:
    json.dump(candidate_json, fp, sort_keys=True, indent=4)