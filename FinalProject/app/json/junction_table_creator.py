
def skill_junctions(candidate_json_keys, candidate_json):
    import pandas as pd
    def strengths_candidate_id_creator(json_keys, json, key):
        """
        Creates a data frame with one column
        :param json_keys:
        :param json:
        :param key:
        :return:
        """
        df_list = []
        for name in json_keys:
            try:
               for item in json[name][key]:
                    df_list.append([json[name]['internal_id'], item])
            except KeyError:
                pass
        df = pd.DataFrame(df_list, columns=['id', 'skill'])
        return df


    def tech_candidate_id_creator(json_keys, json, key):
        """
        Creates a data frame with one column
        :param json_keys:
        :param json:
        :param key:
        :return:
        """
        df_list = []
        for name in json_keys:
            try:
               for item in json[name][key]:
                   df_list.append([json[name]['internal_id'], item, json[name][key][item]])
            except KeyError:
                pass
        df = pd.DataFrame(df_list, columns=['id', 'skill', 'score'])
        return df




    strength_df = strengths_candidate_id_creator(candidate_json_keys, candidate_json, 'strengths')
    weakness_df = strengths_candidate_id_creator(candidate_json_keys, candidate_json, 'weaknesses' )
    tech_skill_df = tech_candidate_id_creator(candidate_json_keys, candidate_json, 'tech_self_score' )
    return strength_df, weakness_df, tech_skill_df, candidate_json
