
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