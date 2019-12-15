from sklearn import metrics


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
