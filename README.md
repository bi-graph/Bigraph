<h1>BiGraph</h1>
<div>
<a href="https://badge.fury.io/py/bigraph"><img src="https://badge.fury.io/py/bigraph.svg" alt="PyPI version" height="18"></a>
<a href="https://www.codacy.com/gh/bi-graph/bigraph/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bi-graph/bigraph&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/e320ed8c06a3466aa9711a138085b9d2" alt="PyPI version" height="18"></a>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/bigraph">

[comment]: <> (<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/bigraph">)

[comment]: <> (<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/bigraph">)

[comment]: <> (<img alt="GitHub search hit counter" src="https://img.shields.io/github/search/bi-graph/bigraph/hit">)

[comment]: <> (<img alt="GitHub search hit counter" src="https://img.shields.io/github/search/bi-graph/bigraph/goto">)

[comment]: <> (<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/bigraph">)

[comment]: <> (<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/bi-graph/bigraph">)

[comment]: <> (<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/bi-graph/bigraph">)
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/bi-graph/bigraph?style=social">
</div>
<p>BiGraph is a Python package for Link prediction in bipartite networks.</p>

<ul>
    <li><b>Bug reports:</b> https://github.com/bi-graph/bigraph/issues</li>
</ul>

> Node based similarities and Katz has been implemented. you can find algorithms in bigraph module. Algorithms implemented so far:

<div align="center">
<table>
<caption><b>Algorithms table</b></caption>
    <tr>
        <td><b>Number</b></td>
        <td align="center"><b>Algorithm</b></td>
    </tr>
    <tr>
        <td align="center">1</td>
        <td><code>jaccard</code></td>
    </tr>
    <tr>
        <td align="center">2</td>
        <td><code>adamic adar</code></td>
    </tr>
    <tr>
        <td align="center">3</td>
        <td><code>common neighbors</code></td>
    </tr>
    <tr>
        <td align="center">4</td>
        <td><code>	preferential attachment</code></td>
    </tr>
    <tr>
        <td align="center">5</td>
        <td><code>katz similarity</code></td>
    </tr>
</table>
</div>

<div>
  <h2>Installation</h2>
  <p>Install the latest version of BiGraph:</p>
  <pre>$ pip install bigraph</pre>
</div>

<div>
<h2>Documentation</h2>
<p> <a href="https://bigraph.readthedocs.io/en/latest/index.html">https://bigraph.readthedocs.io/en/latest/</a></p>

</div>

<h2>Simple example</h2>
<p>Predicting new links in a randomly generated graph using 
<code><b>Adamic-Adar</b></code> algorithm:</p>

```python
from bigraph.predict import aa_predict
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
from bigraph.evaluation.evaluation import evaluate
from bigraph.preprocessing import import_files, make_graph


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
<div>
<h2>Call for Contributions</h2>
<p>The Bigraph project welcomes your expertise and enthusiasm!</p>

<p>Ways to contribute to Bigraph:</p>
<ul>
  <li>Writing code</li>
  <li>Review pull requests</li>
  <li>Develop tutorials, presentations, and other educational materials</li>
  <li>Translate documentation and readme contents</li>
</ul>
</div>

<div>
  <h2>Issues</h2>
  <p>If you happened to encounter any issue in the codes, please report it
    <a href="https://github.com/bi-graph/bigraph/issues">here</a>. 
    A better way is to fork the repository on <b>Github</b> and/or create a pull request.</p>
    
</div>


<h3>Metrics</h3>
<p>Metrics that are calculated during evaluation:</p>

<div>
<table>
<caption><b>Metrics table</b></caption>
    <tr>
        <td><b>Number</b></td>
        <td align="center"><b>Evaluattion metrics</b></td>
    </tr>
    <tr>
        <td align="center">1</td>
        <td><code>Precision</code></td>
    </tr>
    <tr>
        <td align="center">2</td>
        <td><code>AUC</code></td>
    </tr>
    <tr>
        <td align="center">3</td>
        <td><code>ROC</code></td>
    </tr>
    <tr>
        <td align="center">4</td>
        <td><code>returns fpr*</code></td>
    </tr>
    <tr>
        <td align="center">5</td>
        <td><code>returns tpr*</code></td>
    </tr>
</table>
</div>

> * For further usages and calculating different metrics

<h3>Dataset format</h3>
<p>Your dataset should be in the following format (Exclude the 'Row' column):</p>

<div>
<table>
<caption><b>Sample edges (links) dataset</b></caption>
    <tr>
        <td><b>Row</b></td>
        <td align="center"><b>left_side</b></td>
        <td align="center"><b>right_side</b></td>
        <td align="center"><b>Weight*</b></td>
    </tr>
    <tr>
        <td align="center">1</td>
        <td><code>u0</code></td>
        <td><code>v1</code></td>
        <td>1</td>
    </tr>
    <tr>
        <td align="center">2</td>
        <td><code>u2</code></td>
        <td><code>v1</code></td>
        <td>1</td>
    </tr>
    <tr>
        <td align="center">3</td>
        <td><code>u1</code></td>
        <td><code>v2</code></td>
        <td>1</td>
    </tr>
    <tr>
        <td align="center">4</td>
        <td><code>u3</code></td>
        <td><code>v3</code></td>
        <td>1</td>
    </tr>
    <tr>
        <td align="center">5</td>
        <td><code>u4</code></td>
        <td><code>v3</code></td>
        <td>2</td>
    </tr>
</table>
</div>

> * Note that running <pre>
<code>from bigraph.preprocessing import import_files
df, df_nodes = import_files()</code></pre>will create a sample graph for you and will place it in the
<code>inputs</code> directory.
> * Although the weight has not been involved in current version, but, the format will be the same.

<h3>More examples</h3>
<p>Predicting new links in a randomly generated graph using following algorithms:</p>
<ul>
  <li><code><b>Preferential attachment</b></code></li>
  <li><code><b>Jaccard similarity</b></code></li>
  <li><code><b>Common neighbours</b></code></li>
</ul>

```python
from bigraph.predict import pa_predict, jc_predict, cn_predict
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

<div>
<table>
<caption><b>References table</b></caption>
    <tr>
        <td><b>Number</b></td>
        <td align="center"><b>Reference</b></td>
        <td align="center"><b>Year</b></td>
    </tr>
    <tr>
        <td align="center">1</td>
        <td><code>Yang, Y., Lichtenwalter, R.N. & Chawla, N.V. Evaluating link prediction methods. Knowl Inf Syst 45, 751–782 (2015).</code> <a href="https://doi.org/10.1007/s10115-014-0789-0"
target="_blank">https://doi.org/10.1007/s10115-014-0789-0</a></td>
        <td align="center"><b>2015</b></td>
    </tr>
    <tr>
        <td align="center">2</td>
        <td><code>Liben-nowell, David & Kleinberg, Jon. (2003). The Link Prediction Problem for Social Networks. Journal of the American Society for Information Science and Technology.</code><a href="https://doi.org/58.10.1002/asi.20591"
target="_blank">https://doi.org/58.10.1002/asi.20591</a></td>
        <td align="center"><b>2003</b></td>
    </tr>
    <tr>
        <td align="center">2</td>
        <td><code>...</code></td>
        <td align="center"><b>...</b></td>
    </tr>
</table>
</div>

<h3>Future work</h3>

- [x] Modulate the functions
- [ ] Add more algorithms
- [ ] Run on CUDA cores
- [ ] Make it faster using vectorization etc.
- [ ] Add more preprocessors
- [ ] Add dataset, graph, and dataframe manipulations
- [ ] Unify and reconstruct the architecture and eliminate redundancy


<h3>Notes</h3>
<ul>
  <li>
    <code>It can export the graph in .json and .gexf format 
    for further usages. For instance: Gephi etc.</code>
  </li>
</ul>


<h2>If you found it helpful, please give us a <span>:star:</span></h2>

<h2>License</h3>
<p>Released under the BSD license</p>
<div class="footer"><pre>Copyright &copy; 2017-2021 BiGraph Developers
Soran Ghadri (soran.gdr.cs@gmail.com)
Taleb Zarhesh (taleb.zarhesh@gmail.com)</pre>
</div>
