from typing import Union

import pandas as pd


def import_files() -> Union[dict, dict]:
    """
    Import links and labels from csv files
    :return: links and label dataframes
    """
    print('Importing files and making dataframes...')
    raw_adjacency_dictionary = pd.read_csv('./inputs/neighbour_matrix.csv', sep=',')
    raw_label_dictionary = pd.read_csv('./inputs/id_labels.csv', sep=',')
    # raw_adjacency_dictionary = raw_adjacency_dictionary.drop(['Weight'], axis=1)

    label_dictionary = {}
    for row in raw_label_dictionary.iterrows():
        label_dictionary.update({row[1][0]: row[1][1]})
    return raw_adjacency_dictionary, label_dictionary
