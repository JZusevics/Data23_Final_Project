from FinalProject.app.transform.save_cleaned_files import *

if __name__ == '__main__':

    reset_schema('schema.txt')

    # with open('data.json') as f:
    #     extracted1 = json.loads(f.read())
    # extracted0 = pd.read_csv('academy.csv')
    # extracted2 = pd.read_csv('txt.csv')
    # extracted3 = pd.read_csv('talent.csv')
    # extracted = [extracted0, extracted1, extracted2, extracted3]

    extracted_list = []
    extracted = extract_all(extracted_list)
    clean_and_load(extracted)
    pass;
