
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