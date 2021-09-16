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



# ******* CANDIDATE INFO **********
def load_candidate_info(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO candidate_info (candidate_id, applicant_day_trainee_id, invited_by_id, trainer_id, first_name, "
            "middle_name, last_name, dob, gender, phone_number, university, degree, address, city, postcode, email) "
            "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            int(row.candidate_id), int(row.applicant_day_trainee_id), row.inviter_id, row.trainer_id, row.first_name,
            row.middle_name, row.last_name, row.date_of_birth, row.gender, row.phone_number, row.university, row.degree,
            row.address, row.city, row.postcode, row.email)
    CNXN.commit()



def load_inviter(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO inviter (invited_by_id, invited_by_name) "
            "values(?,?)",
            row[0], row[1])
    CNXN.commit()



def load_trainer(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO trainer (trainer_id, trainer_name) "
            "values(?,?)",
            row[0], row[1])
    CNXN.commit()



def load_course_junc(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO course_junc (candidate_id, course_id) "
            "values(?,?)",
            int(row[0]), int(row[1]))
    CNXN.commit()



def load_course_info(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO course_info (course_id, course_stream, course_no, course_start) "
            "values(?,?,?,?)",
            int(row.course_id), row.course_name, int(row.course_number), row.course_start_date)
    CNXN.commit()



# ******* ACADEMY DAY **********
def load_academy_performance(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO academy_performance (candidate_id, week, sparta_skill_id, score) "
            "values(?,?,?,?)",
            int(row.candidate_id), int(row.week), int(row.sparta_skill_id), int(row.score))
    CNXN.commit()



def load_sparta_skill(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO sparta_skill (sparta_skill_id, skill_name) "
            "values(?,?)",
            row.sparta_skill_id, row.skill_name)
    CNXN.commit()



# ******* STRENGTH **********
def load_strength(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO strength (strength_id, strength) "
            "values(?,?)",
            row[0], row[1])

    CNXN.commit()


def load_strength_junc(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO strength_junc (candidate_id, strength_id) "
            "values(?,?)",
            int(row.candidate_id), int(row[1]))
    CNXN.commit()



# ******* WEAKNESS **********
def load_weakness(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO weakness (weakness_id, weakness) "
            "values(?,?)",
            row[0], row[1])
    CNXN.commit()


def load_weakness_junc(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO weakness_junc (candidate_id, weakness_id) "
            "values(?,?)",
            int(row[0]), int(row[1]))
    CNXN.commit()



# ******* TECH SKILL **********
def load_tech_self_score(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO tech_self_score (candidate_id, tech_skill_id, score) "
            "values(?,?,?)",
            int(row.candidate_id), int(row.skill_id), int(row.score))
    CNXN.commit()



def load_tech_skill(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO tech_skill (tech_skill_id, skill_name) "
            "values(?,?)",
            row[0], row[1])
    CNXN.commit()



# ******* SPARTA DAY **********
def load_sparta_day_performance(df):
    for index, row in df.iterrows():
        print(index)
        CURSOR.execute(
            "INSERT INTO TestTable (candidate_id, day_id, psychometric_score, presentation_score, "
            "financial_support, pass, course_interest, geo_flex, self_development) "
            "values(?,?,?,?,?,?,?,?,?)",
            row.candidate_id, row.day_id, row.psychometric_score, row.presentation_score, row.financial_support_self,
            row['pass'], row.course_interest, row.geo_flex, row.self_development)
    CNXN.commit()


def load_sparta_day(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO sparta_day (sparta_day_id, applicant_day_date_id, location_id) "
            "values(?,?,?)",
            int(row[0]), int(row[1]), int(row[2]))
    CNXN.commit()


def load_applicant_day_date(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO applicant_day_date (applicant_day_date_id, applicant_day_date) "
            "values(?,?)",
            row.applicant_day_date_id, row.applicant_day_date)
    CNXN.commit()


def load_test_location(df):
    for index, row in df.iterrows():
        CURSOR.execute(
            "INSERT INTO test_location (location_id, location_name) "
            "values(?,?)",
            int(row[0]), row[1])
    CNXN.commit()


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


if __name__ == '__main__':
    load_test()
