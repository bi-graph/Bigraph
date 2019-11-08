
def import_files():
    """

    :return:
    """
    df = pd.read_csv('./inputs/SNP-Cancer Dataset.csv', sep=',')
    df_nodes = pd.read_csv('./inputs/id_labels.csv', sep=',')
    # df = df.drop(['Weight'], axis=1)