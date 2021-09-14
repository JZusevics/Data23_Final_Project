from FinalProject.config_manager import *
from FinalProject.app.extract.extract_talent_csv import *


# ******* CANDIDATE ID GEN **********
# Each function takes in a Data Frame and inserts each row into the corresponding SQL table
def load_candidate_id_gen(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (candidate_name, sparta_day_date, candidate_id) "
            "values(?,?,?)",
            row.candidate_name, row.sparta_day_date, row.candidate_id)
    CNXN.commit()
    CURSOR.close()


# ******* CANDIDATE INFO **********
def load_candidate_info(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (candidate_id, invited_by_id, trainer_id, application_day_trainee_id, first_name, "
            "middle_name, last_name, dob, gender, phone_number, university, degree, address, city, postcode, email) "
            "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row.candidate_id, row.invited_by_id, row.trainer_id, row.application_day_trainee_id, row.first_name,
            row.middle_name, row.last_name, row.dob, row.gender, row.phone_number, row.university, row.degree,
            row.address, row.city, row.postcode, row.email,)
    CNXN.commit()
    CURSOR.close()


def load_inviter(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (invited_by_id, invited_by_name) "
            "values(?,?)",
            row.invited_by_id, row.invited_by_name)
    CNXN.commit()
    CURSOR.close()


def load_trainer(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (trainer_id, trainer_name) "
            "values(?,?)",
            row.trainer_id, row.trainer_name)
    CNXN.commit()
    CURSOR.close()

def load_course_junc(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (candidate_id, course_id) "
            "values(?,?)",
            row.candidate_id, row.course_id)
    CNXN.commit()
    CURSOR.close()

def load_course_info(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (course_id, course_stream, course_no, course_start) "
            "values(?,?,?,?)",
            row.course_id, row.course_stream, row.course_no, row.course_start)
    CNXN.commit()
    CURSOR.close()


# ******* ACADEMY DAY **********
def load_academy_performance(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (candidate_id, week, sparta_skill_id, score) "
            "values(?,?,?,?)",
            row.candidate_name, row.sparta_day_date, row.candidate_id, row.score)
    CNXN.commit()
    CURSOR.close()


def load_sparta_skill(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (sparta_skill_id, skill_name) "
            "values(?,?)",
            row.sparta_skill_id, row.skill_name)
    CNXN.commit()
    CURSOR.close()


# ******* STRENGTH **********
def load_strength(df):
    for index, row in df.iterrows():
        print(row.name, row['strength_ids'])
        CURSOR.execute(
            "INSERT INTO strength (strength_id, strength) "
            "values(?,?)",
            row.name, row['strength_ids'])

    CNXN.commit()
    #CURSOR.close()


def load_strength_junc(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO strength_junc (candidate_id, strength_id) "
            "values(?,?)",
            row.candidate_id, row.strength_id)
    CNXN.commit()
    CURSOR.close()


# ******* WEAKNESS **********
def load_weakness(df):
    for index, row in df.iterrows():
        print(row.name, row['weakness_ids_df'])
        CURSOR.execute(
            "INSERT INTO weakness (weakness_id, weakness) "
            "values(?,?)",
            row.name, row['weakness_ids_df'])
    CNXN.commit()


def load_weakness_junc(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO weakness_junc (candidate_id, weakness_id) "
            "values(?,?)",
            row.candidate_id, row.weakness_id)
    CNXN.commit()
    CURSOR.close()


# ******* TECH SKILL **********
def load_tech_self_score(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO tech_self_score (candidate_id, tech_skill_id, score) "
            "values(?,?,?)",
            row.candidate_id, row.tech_skill_id, row.score)
    CNXN.commit()
    CURSOR.close()


def load_tech_skill(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO tech_skill (tech_skill_id, skill_name) "
            "values(?,?)",
            row.name, row['tech_skill_ids_df'])
    CNXN.commit()
    CURSOR.close()


# ******* SPARTA DAY **********
def load_sparta_day_performance(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (candidate_id, sparta_day_id, psychometric_score, presentation_score, "
            "financial_support, result, course_interest, geo_felx, self_development) "
            "values(?,?,?,?,?,?,?,?,?)",
            row.candidate_id, row.sparta_day_id, row.psychometric_score, row.presentation_score, row.financial_support,
            row.result, row.course_interest, row.geo_felx, row.self_development)
    CNXN.commit()
    CURSOR.close()


def load_sparta_day(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (sparta_day_id, applicant_day_date_id, location_id) "
            "values(?,?,?)",
            row.sparta_day_id, row.applicant_day_date_id, row.location_id)
    CNXN.commit()
    CURSOR.close()


def load_applicant_day_date(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (applicant_day_date_id, applicant_day_date) "
            "values(?,?)",
            row.applicant_day_date_id, row.applicant_day_date)
    CNXN.commit()
    CURSOR.close()


def load_test_location(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (location_id, location_name) "
            "values(?,?)",
            row.location_id, row.location_name)
    CNXN.commit()
    CURSOR.close()










##########################################################################
# TESTING
def load_test():

    df = extract_csv('Talent/April2019Applicants.csv')
    df1 = df.where(pd.notnull(df), None)

    for index, row in df1.iterrows():
        CURSOR.execute(
            "INSERT INTO TestTable (id, name, gender, dob, email, city, address,"
            "postcode, phone_number, uni, degree, invited_date, month, invited_by) "
            "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row.id, row['name'], row.gender, row.dob, row.email, row.city, row.address, row.postcode,
            row.phone_number, row.uni, row.degree, row.invited_date, row.month, row.invited_by)

    CNXN.commit()
    CURSOR.close()




if __name__ == '__main__':
    load_test()
