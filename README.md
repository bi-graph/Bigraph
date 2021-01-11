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
  

<h2>Simple example</h2>

<p>You can try other provided prediction algorithms by replacing the `aa_predict()` function.</p>

```python
from bigraph.bigraph import aa_predict
from bigraph.preprocessing import import_files, make_graph

def adamic_adar_prediction():
    """
    Link prediction on a bipartite network
    :return: Predicted linkes
    """

    df, df_nodes = import_files()
    print(df)
    print(f"Graph Nodes: ", df_nodes)
    G = make_graph(df)
    print(G)
    aa_predict(G)  # Here we have called Adamic Adar method from bigraph module

# Executing the function
if __name__ == '__main__':
    adamic_adar_prediction()
```
<p>or you can run evaluation methods directly which calls its peer method automatically.</p>

```python
from bigraph.evaluation import evaluate
from bigraph.preprocessing import import_files, make_graph, check_input_files

def adamic_adar_evaluation():
    """

    :return:
    """
    df, df_nodes = import_files()
    G = make_graph(df)
    evaluate(G, k=10,
             method='aa')  # Here we have evaluated adamic-adar
    # methods using evaluation module. Methods are 'jc', 'aa', 'pa', 'cn'

# Executing the function
if __name__ == '__main__':
    adamic_adar_evaluation()
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
from bigraph.bigraph import pa_predict, jc_predict, cn_predict
from bigraph.preprocessing import import_files, make_graph

def main():
  """
  Link prediction on a bipartite network
  :return: Predicted linkes
  """
  df, df_nodes = import_files()
  G = make_graph(df)
  pa_predict(G)  # Prefferencial attachment
  jc_predict(G)  # Jaccard coefficient
  cn_predict(G)  # Common neighbors

# Executing the function
if __name__ == '__main__':
    main()
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
