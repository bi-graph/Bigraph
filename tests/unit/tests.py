import unittest

import bigraph


class TestAAPredict(unittest.TestCase):
    def test_aa_predict(self):
        bg = bigraph.BiGraph()
        output = bg.aa_predict()
        print(output)
        self.assertEqual(type(output), dict, "Not a dict")


if __name__ == "__main__":
    unittest.main()
