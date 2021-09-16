import json
from extract_all import *
extracted_list = []
extracted = extract_all(extracted_list)

extracted[0].to_csv('academy.csv')

extracted[2].to_csv('txt.csv')

extracted[3].to_csv('talent.csv')
with open('../../data.json', 'w', newline='') as fp:
    json.dump(extracted[1], fp, sort_keys=True, indent=4)
