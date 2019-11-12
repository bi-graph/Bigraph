def add_to_list(df):
    """

    :param df:
    :return:
    """
    edgeList = []
    for i in df.iterrows():
        # if not str(df_nodes[i[1][1]]).__contains__('.'):
        tuples = i[1][0], i[1][1]
        edgeList.append(tuples)
    return edgeList
