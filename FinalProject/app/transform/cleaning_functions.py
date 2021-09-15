from FinalProject.config_manager import *

def split_names(df: pd.DataFrame):
    """
    :param df: A dataframe which name column will be transformed
    :return: df: Returns the df with the transformed collumns
    """
    # create variables
    last_name_prefix = ["Van", "Le", "Di", "O", "De", "Du", "Von", "St", "Mc", "Mac", "La"]
    first_name = []
    middle_name = []
    last_name = []

    df["name"] = df['name'].str.replace(" '", "'")
    df["name"] = df['name'].str.replace("' ", "'")
    df["name"] = df['name'].str.replace(" - ", "'")

    for name in df["name"]:
        # Split names on spaces
        split_name = name.split()
        for index, name in enumerate(split_name):
            split_name[index] = name.title()
        # If more than 2 names
        if len(split_name) > 2:
            # If the first name and second name are the same put them together
            if split_name[0] == split_name[1]:
                split_name = [" ".join(split_name[0:2])] + split_name[2:]
            # If name contains a prefix put the following names together
            for sub_name in last_name_prefix:
                if sub_name in split_name:
                    # Check if prefix is in the first name only put first and second together
                    if split_name.index(sub_name) == 0:
                        split_name = ["".join(split_name[split_name.index(sub_name):2])]+ split_name[2::]
                    if sub_name in split_name:
                        split_name = split_name[0:split_name.index(sub_name)]+[" ".join(split_name[split_name.index(sub_name)::])]

        first_name.append(split_name[0].title())
        last_name.append(split_name[-1].title())
        if len(split_name) == 2:
            middle_name.append(numpy.nan)
        else:
            middle_name.append("".join(split_name[1:-1]).title())

    df.insert(1, "first_name", first_name, True)
    df.insert(2, "middle_name", middle_name, True)
    df.insert(3, "last_name", last_name, True)
    df.drop(columns="name", inplace=True)
    return df