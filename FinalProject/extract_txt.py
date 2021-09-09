def extract_txt(obj):
    """

    :param obj: the object from s3
    :return: Data Frame from the txt file
    """
    # get s3 object
    s3_object = s3_client.get_object(
                    Bucket=bucket_name,
                    Key=obj['Key']
                )

    # store txt file as string
    text_file = s3_object['Body'].read().decode('utf-8')
    # separate date, location and candidate info in lists
    lines = text_file.splitlines()
    # Store date in date format
    date = datetime.strptime(lines[0], "%A %d %B %Y").date()
    location = lines[1]
    # from 3rd line data has name, psychometrics and presentation scores
    candidate_data = lines[3:-1]

    # create variables for separating candidate data
    names = []
    scores=[]
    # separate string to obtain names and scores as strings
    for item in candidate_data:
        names.append(item[:(item.index("Psychometrics"))-4])
        scores.append(item[item.index("Psychometrics"):])

    # create empty lists for psychometrics and presentation as strings
    psychometrics = []
    presentation = []
    # separate score into presentation and pyschometrics scores
    for score_line in scores:
        scores_seperated = score_line.split(',')
        psychometrics.append(scores_seperated[0].replace("Psychometrics: ", "").strip())
        presentation.append(scores_seperated[1].replace("Presentation: ", "").strip())

    # Find percentage of psychometrics scores and store in list
    psychometrics_score = []
    for score in psychometrics:
        psychometrics_score_list = score.split("/")
        psychometrics_score_list = round((int(psychometrics_score_list[0]) / int(psychometrics_score_list[1]) * 100), 2)
        psychometrics_score.append(psychometrics_score_list)

    # Find percentage of presentation scores and store in list
    presentation_score = []
    for score in presentation:
        presentation_score_list = score.split("/")
        presentation_score_list = round((int(presentation_score_list[0]) / int(presentation_score_list[1]) * 100), 2)
        presentation_score.append(presentation_score_list)

    # Concatenate columns for Name, Scores, Date and Location into a dataframe
    df = pd.DataFrame(names, columns=["Names"])
    df.insert(1, "Psychometrics Score", psychometrics_score, True)
    df.insert(2, "Presentation Score", presentation_score, True)
    df.insert(3, "Date", date, True)
    df.insert(4, "Location", location, True)

    return df