from FinalProject.config_manager import *


def reset_schema(txt_file):
    """
     Function reads the Schema.txt file as an SQL command

     Resets the SQL tables dropping ALL the Data
    """
    with open(txt_file) as f:
        lines = f.read()
    CURSOR.execute(lines)
    CNXN.commit()


if __name__ == '__main__':
    reset_schema()
