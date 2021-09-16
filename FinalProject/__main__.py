from FinalProject.app.transform.save_cleaned_files import *

if __name__ == '__main__':
    reset_schema('schema.txt')
    extracted_list = []
    extracted = extract_all(extracted_list)
    clean_and_load(extracted)
    pass


