import csv
import os
import pathlib
import random
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
    _check_input_files(edge_csv, label_id)
    raw_adjacency_dictionary = pd.read_csv(edge_csv, sep=sep, *args, **kwargs)
    raw_label_dictionary = pd.read_csv(label_id, sep=sep, *args, **kwargs)
    # raw_adjacency_dictionary = raw_adjacency_dictionary.drop(['Weight'], axis=1)
    label_dictionary = {}
    for row in raw_label_dictionary.iterrows():
        label_dictionary.update({row[1][0]: row[1][1]})
    return raw_adjacency_dictionary, label_dictionary


def _check_input_files(edge_csv: str, label_id: str) -> bool:
    """
    Check if there is any input file.

    :param edge_csv: Path to the edge-list csv file
    :param label_id: Path to the label-id-list csv file
    :return: True on finishing successfully
    """
    pathlib.Path('./inputs').mkdir(parents=True, exist_ok=True)
    right_nodes_count = random.randint(20, 30)
    left_nodes_count = random.randint(30, 40)
    if edge_csv == "./inputs/neighbour_matrix.csv":
        file_exists = os.path.isfile("./inputs/neighbour_matrix.csv")
        if not file_exists:
            _generate_random_graph_edges(left_nodes_count, right_nodes_count)
    if label_id == "./inputs/id_labels.csv":
        file_exists = os.path.isfile("./inputs/id_labels.csv")
        if not file_exists:
            _generate_random_graph_labels(left_nodes_count, right_nodes_count)
    return True


def _generate_random_graph_labels(left_nodes_count: int, right_nodes_count: int) -> bool:
    """
    Generate Labels for randomly generated graph nodes by generate_random_graph_edges() function

    :param left_nodes_count: Number of the left-side nodes
    :param right_nodes_count: Number of the right-side nodes
    :return: True on success
    """
    with open('./inputs/id_labels.csv', 'w') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(['ID', 'Label'])
        for i in range(left_nodes_count):
            file_writer.writerow([i, f"left_node_{i}"])
        for i in range(right_nodes_count):
            file_writer.writerow([i + 100, f"right_node_{i}"])
    return True


def _generate_random_graph_edges(left_nodes_count: int, right_nodes_count: int) -> bool:
    """
    Generate a random graph and write it to a CSV file

    :param left_nodes_count: Number of the left-side nodes
    :param right_nodes_count: Number of the right-side nodes
    :return: True on success
    """
    with open('./inputs/neighbour_matrix.csv', 'w') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rand_seed = right_nodes_count * left_nodes_count - ((right_nodes_count * left_nodes_count) / 3)
        rand_seed2 = right_nodes_count * left_nodes_count
        links_count = random.randint(int(rand_seed), int(rand_seed2))
        file_writer.writerow(['left_side', 'right_side', 'Weight'])
        for i in range(links_count):
            file_writer.writerow(
                [random.randint(0, left_nodes_count), random.randint(0, right_nodes_count) + 100,
                 random.randint(1, 3)])

    return True
