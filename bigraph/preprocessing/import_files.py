from typing import Union

import pandas as pd


def import_files(
        edge_csv: str = "./inputs/neighbour_matrix.csv",
        label_id: str = "./inputs/id_labels.csv",
        sep: str = ',',
        *args,
        **kwargs
) -> Union[dict, dict]:
    """
    Import links and labels from csv files
    :param edge_csv: A CSV file containing edge data on each line:
        0,4,2 that are u,v,w which stand for node 1, node 2, weight respectively
    :param label_id: A CSV file containing labels for nodes:
        10,node_name which are ID,label for each node
    :param sep: A separator that is the boundary for distinct entities
    :return: links and label dataframes
    """
    print('Importing files and making dataframes...')
    raw_adjacency_dictionary = pd.read_csv(edge_csv, sep=sep, *args, **kwargs)
    raw_label_dictionary = pd.read_csv(label_id, sep=sep, *args, **kwargs)
    # raw_adjacency_dictionary = raw_adjacency_dictionary.drop(['Weight'], axis=1)

    label_dictionary = {}
    for row in raw_label_dictionary.iterrows():
        label_dictionary.update({row[1][0]: row[1][1]})
    return raw_adjacency_dictionary, label_dictionary
