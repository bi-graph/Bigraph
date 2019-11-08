import pandas as pd

def import_files():
    """

    :return:
    """
    df = pd.read_csv('./inputs/SNP-Cancer Dataset.csv', sep=',')
    df_nodes = pd.read_csv('./inputs/id_labels.csv', sep=',')
    # df = df.drop(['Weight'], axis=1)

    dic = {}
    for row in df_nodes.iterrows():
        dic.update({row[1][0]: row[1][1]})