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
from predictionMethods import predict as pr

def main():
    """
    Link prediction on a bipartite network
    :return: your desired method output
    """
    df, df_nodes = import_files()
    G = make_graph(df, df_nodes)
    pr.aa_predict(G, df_nodes) # Here we have called Adamic Adar method from predict module

```
or you can run evaluation methods directly which calls its peer method automatically

```python
from evaluation import evaluation as ev

def main():
    """
    Link prediction on a bipartite network
    :return: your desired method output
    """
    df, df_nodes = import_files()
    G = make_graph(df, df_nodes)
    graphEdges = G.edges
    ev.evaluateROC(G,df_nodes, graphEdges, method='jc', k=10) # Here we have evaluated Jaccard method using evaluation module. Methods are 'jc', 'aa', 'pa', 'cn'

```

### Documentation
I will provide documentations whenever I could make time!:watch:

> 1. After running the main, it will exports the graph in .json and .gexf format for furthur usages

<h3>:heart:If it was helpful then please hit the <span>:star:</span> button!:heart:</h3>
