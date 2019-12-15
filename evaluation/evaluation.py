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