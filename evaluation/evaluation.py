from more_itertools import tabulate
from pandas.tests.extension.numpy_.test_numpy_nested import np
from sklearn import metrics
from sklearn.model_selection import KFold


def plot_ROC(fpr, tpr, met):
    """

    :param fpr:
    :param tpr:
    :param met:
    :return:
    """
    # Print AUC
    auc = metrics.auc(fpr, tpr)
    # auc = np.trapz(tpr, fpr)
    print('AUC:', auc)
    # Print ROC curve
    plt.plot(fpr, tpr, label='AUC -> %s (area = %0.2f)' % (met, auc))
    # plt.show()
    return True

def _evaluate_method(G, k, method):
    """

    :param G:
    :param k:
    :param method:
    :return:
    """
    kf = KFold(n_splits=k, shuffle=True)
    precision_sum = 0
    auc_sum = 0
    print(tabulate([[f'Starting caculating {method}']], tablefmt='grid'))
    iterator = 0

    for train_index, test_index in kf.split(list(G.edges)):
        G_train = G.copy()
        np_edges = np.array(list(G.edges))
        test_edges = np_edges[test_index]
        G_train.remove_edges_from(test_edges)
        # print('G_train(node, edge): ', G_train.number_of_nodes(), G_train.number_of_edges())
        print('Iteration %i / %i :' % (iterator, k))
        # -------------------------------------------------------------------
        if method == 'jc':
            predicted = pr.jc_predict(G_train)
        elif method == 'aa':
            predicted = pr.aa_predict(G_train)
        elif method == 'cn':
            predicted = pr.cn_predict(G_train)
        elif method == 'pa':
            predicted = pr.pa_predict(G_train)
        else:
            raise Exception('Entered method is not valid', method)
        # -------------------------------------------------------------------
        precision = len(set(predicted.keys()) & set(map(tuple, test_edges))) / len(set(predicted.keys()))
        precision_sum += precision
        print('precision: ', precision)

        # -------------------------------------------------------------------

        score_algo, label_algo = zip(*[(float(score), label in test_edges) for label, score in
                                       sorted(predicted.items(), key=itemgetter(1), reverse=True)])
        # Compute the ROC AUC Score
        fpr_algo, tpr_algo, _ = roc_curve(label_algo, score_algo)
        auc_algo = roc_auc_score(label_algo, score_algo)
        print("auc: ", auc_algo)
        auc_sum += auc_algo
        # -------------------------------------------------------------------
        iterator += 1
        print('---' * 20)

    overal_precision = precision_sum / k
    overal_auc = auc_sum / k
    print(tabulate([["%i-fold evaluation overal precision: %f" % (k, overal_precision),
                     "%i-fold evaluation overal auc: %f" % (k, overal_auc)]], tablefmt='jira'))
    headers = ['overal_precision', 'overal_auc']
    table = [[overal_precision, overal_auc]]
    print(tabulate(table, headers, tablefmt="pipe"))
    return [overal_precision, overal_auc, fpr_algo, tpr_algo]

def evaluate(G, k=2, method='all'):
    """

    :param G:
    :param k:
    :param method:
    :return:
    """
    methods = ['cn', 'jc', 'aa', 'pa']
    results = {}
    if method == 'all':
        for _method in methods:
            result = _evaluate_method(G, k, _method)
            results.update({method: result})
