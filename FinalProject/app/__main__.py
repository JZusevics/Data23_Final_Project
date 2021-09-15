from extract_functions.extract_all import *
from json.datacleaningjson import clean
extracted = extract_all()
extracted_txt = extracted[2]
step1 = clean_location(extracted_txt)
step2 = split_names(step1)
transformed_txt = cand_id_gen_txt(step2)

clean(transformed_txt)