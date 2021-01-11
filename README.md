<h1>BiGraph</h1>
<p>BiGraph is a Python package for the creation, Link prediction, and 
evaluation of bipartite networks.</p>

<ul>
<li><b>Bug reports:</b> https://github.com/bi-graph/bigraph/issues</li>
</ul>

> Node based similarities and Katz has been implemented. you can find algorithms in bigraph module.
Algorithms implemented so far:
  

  
  | Number  | Algorithm           |
  | ------------- | -------------            |
  |       1.     |  `adamic adar`             |
  |       2.     | `common neighbors `        |
  |       3.     | `preferential attachment`  |
  |       4.     | `jaccard  `                |
  |       5.     | `katz similarity`          |
  

<h2>Simple example</h2>
<p>Predicting new links in a randomly generated graph using 
<code><b>Adamic-Adar</b></code> algorithm:</p>

```python
from bigraph.bigraph import aa_predict
from bigraph.preprocessing import import_files, make_graph

def adamic_adar_prediction():
    """
    Link prediction on bipartite networks
    :return: A dictionary containing predicted links
    """

    df, df_nodes = import_files()
    print(df)
    print(f"Graph Nodes: ", df_nodes)
    G = make_graph(df)
    print(G)
    predicted = aa_predict(G)  # Here we have called Adamic Adar method from bigraph module
    return predicted

# Executing the function
if __name__ == '__main__':
    adamic_adar_prediction()
```
<p>Evaluating <code><b>Adamic-Adar</b></code> algorithm.<br>
You can try other provided prediction algorithms by replacing the <b>"aa"</b> argument.</p>

```python
from bigraph.evaluation import evaluate
from bigraph.preprocessing import import_files, make_graph, check_input_files

def adamic_adar_evaluation():
    """
    Evaluate Adamic-Adar algorithm using 10-Fold cross-validation 
    :return: A dictionary containing the evaluation results
    """
    df, df_nodes = import_files()
    G = make_graph(df)
    results = evaluate(G, k=10,
             method='aa')  # Here we have evaluated adamic-adar
    # methods using evaluation module. Methods are 'jc', 'aa', 'pa', 'cn'
    return results

# Executing the function
if __name__ == '__main__':
    adamic_adar_evaluation()
```
<h3>Metrics</h3>
<p>Metrics that are calculated during evaluation:</p>

| Number  | Evaluattion metrics           |
  | ------------- | -------------            |
  |       1.     |  `Precision`             |
  |       2.     | `AUC`        |
  |       3.     | `ROC`  |
  |       4.     | `returns fpr*`                |
  |       5.     | `returns tpr*`          |

> * For further usages and calculating different metrics

<h3>Dataset format</h3>
<p>Your dataset should be in the following format:</p>

| Row  | Left side element | Right side element | Weight* |
  | ------------- | ------------- | --- | --- |
  |       1.     | `u0` | `v1` | 1 |
  |       2.     | `u2` | `v1` | 1 |
  |       3.     | `u1` | `v2`| 1 |
  |       4.     | `u3` | `v3` | 1|
  |       5.     | `u4` | `v3` | 2 |

> * Although the weight has not been involved in current version, but, the format will be the same.

<h3>More examples</h3>
<p>Predicting new links in a randomly generated graph using following algorithms:</p>
<ul>
  <li><code><b>Preferential attachment</b></code></li>
  <li><code><b>Jaccard similarity</b></code></li>
  <li><code><b>Common neighbours</b></code></li>
</ul>

```python
from bigraph.bigraph import pa_predict, jc_predict, cn_predict
from bigraph.preprocessing import import_files, make_graph

def main():
  """
  Link prediction on bipartite networks
  :return:
  """
  df, df_nodes = import_files()
  G = make_graph(df)
  pa_predict(G)  # Preferential attachment
  jc_predict(G)  # Jaccard coefficient
  cn_predict(G)  # Common neighbors

# Executing the function
if __name__ == '__main__':
    main()
```
<h3>References</h3>

| Number  | Reference           |
  | ------------- | -------------            |
  |       1.     |  `Yang, Y., Lichtenwalter, R.N. & Chawla, N.V. Knowl Inf Syst (2015) 45: 751.` https://doi.org/10.1007/s10115-014-0789-0             |
  |       2.     | `Liben-nowell, David & Kleinberg, Jon. (2003). The Link Prediction Problem for Social Networks. Journal of the American Society for Information Science and Technology.` https://doi.org/58.10.1002/asi.20591 |
  |       3.     | `...`  |
  
<h3>Future work</h3>

- [x] Modulate the functions
- [ ] Make it faster using vectorization etc.
- [ ] Unify and reconstruct the architecture and eliminate redundancy

<h3>Documentation</h3>
<p>Comming soon</p>

<pre><ul><li>It can export the graph in .json and .gexf format 
for furthur usages. For instance: Gephi etc.</li></ul></pre>

<h3>If it was helpful then hit the <span>:star:</span></h3>

<div class="footer">
        &copy; 2021 BiGraph Developers
</div>

