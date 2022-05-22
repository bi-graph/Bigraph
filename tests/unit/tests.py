import unittest

from bigraph.predict import aa_predict
from bigraph.preprocessing import import_files, make_graph

df, df_nodes = import_files.import_files()
G = make_graph.make_graph(df)


class TestAAPredict(unittest.TestCase):
    def test_aa_predict(self):
        output = aa_predict(G)
        print(output)
        self.assertEqual(type(output), dict, "Not a dict")


if __name__ == "__main__":
    unittest.main()
