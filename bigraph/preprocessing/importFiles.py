from typing import Union

import pandas as pd


def import_files(
        adjacency_matrix: str = "./inputs/neighbour_matrix.csv",
        label_id: str = "./inputs/id_labels.csv",
        sep: str = ","
) -> Union[dict, dict]:
    """
    Import links and labels from csv files
    :return: links and label dataframes
    """
    print('Importing files and making dataframes...')
    raw_adjacency_dictionary = pd.read_csv(adjacency_matrix, sep=sep)
    raw_label_dictionary = pd.read_csv(label_id, sep=sep)
    # raw_adjacency_dictionary = raw_adjacency_dictionary.drop(['Weight'], axis=1)

    label_dictionary = {}
    for row in raw_label_dictionary.iterrows():
        label_dictionary.update({row[1][0]: row[1][1]})
    return raw_adjacency_dictionary, label_dictionary
