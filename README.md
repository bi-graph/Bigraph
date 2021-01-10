# Bipartite link prediction </h1>

Predicting links in bipartite networks on top of networkx

> Node based similarities and Katz has been implemented. you can find algorithms in prediction directory.
Algorithms untill now:
  

  
  | Number  | Algorithm           |
  | ------------- | -------------            |
  |       1.     |  `adamic adar`             |
  |       2.     | `common neighbors `        |
  |       3.     | `preferential attachment`  |
  |       4.     | `jaccard  `                |
  |       5.     | `katz similarity`          |
  

### How to use the code
you can run the code by placing your data in inputs folder and use predict methodes iplemented in "predict" file or directly call provided functions in the evaluation file.

```python
from bigraph import bigraph as bg

def main():
  """
  Link prediction on a bipartite network
  :return: Predicted linkes
  """
  df, df_nodes = import_files()
  G = make_graph(df)
  pr.aa_predict(G)  # Here we have called Adamic Adar method from bigraph module

```
or you can run evaluation methods directly which calls its peer method automatically

```python
from bigraph.evaluation import evaluation as ev


def main():
    """
    Link prediction on a bipartite network
    :return: Predicted linkes
    """
    df, df_nodes = import_files()
    G = make_graph(df)
    ev.evaluate(G, k=10,
                method='all')  # Here we have evaluated all methods using evaluation module. Methods are 'jc', 'aa', 'pa', 'cn'

```
### Metrics
Metrics that are calculated during evaluation:

| Number  | Evaluattion metrics           |
  | ------------- | -------------            |
  |       1.     |  `Precision`             |
  |       2.     | `AUC`        |
  |       3.     | `ROC`  |
  |       4.     | `returns fpr*`                |
  |       5.     | `returns tpr*`          |

> * For further usages and calculating different metrics

### Dataset format
Your dataset should be in the following format:

| Row  | Left side element | Right side element | Weight* |
  | ------------- | ------------- | --- | --- |
  |       1.     | `ll0` | `rl1` | 1 |
  |       2.     | `ll2` | `rl1` | 1 |
  |       3.     | `ll1` | `rl2`| 1 |
  |       4.     | `ll3` | `rl3` | 1|
  |       5.     | `ll4` | `rl3` | 2 |

> * Although the weight has not been involved in current version, but, the format will be the same.
### More examples

```python
from bigraph import bigraph as bg


def main():
  """
  Link prediction on a bipartite network
  :return: Predicted linkes
  """
  df, df_nodes = import_files()
  G = make_graph(df)
  pr.aa_predict(G)  # Here we have called Adamic Adar method from bigraph module
  pr.pa_predict(G)  # Prefferencial attachment
  pr.jc_predict(G)  # Jaccard coefficient
  pr.cn_predict(G)  # Common neighbors

```
### References

| Number  | Reference           |
  | ------------- | -------------            |
  |       1.     |  `Yang, Y., Lichtenwalter, R.N. & Chawla, N.V. Knowl Inf Syst (2015) 45: 751.` https://doi.org/10.1007/s10115-014-0789-0             |
  |       2.     | `Liben-nowell, David & Kleinberg, Jon. (2003). The Link Prediction Problem for Social Networks. Journal of the American Society for Information Science and Technology.` https://doi.org/58.10.1002/asi.20591 |
  |       3.     | `...`  |
  
### TODO
- [x] Modulate the functions
- [ ] Make it faster using vectorization etc.
- [ ] Unify and reconstruct the architecture and eliminate redundancy

### Documentation
I will provide documentations whenever I could make time!:watch: or you can pull a request and help to make it happen together

> 1. After running the main, it will export the graph in .json and .gexf format for furthur usages. For instance: Gephi etc.

<h3>If it was helpful then hit the <span>:star:</span></h3>
