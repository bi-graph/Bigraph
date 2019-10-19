from _operator import itemgetter

import networkx as nx
from matplotlib import pyplot as plt
from sklearn import metrics

from predictionMethods.predict import jc_predict, aa_predict, cn_predict, pa_predict


def plot_ROC(fpr, tpr, met):
    # Print AUC
    auc = metrics.auc(fpr, tpr)
    # auc = np.trapz(tpr, fpr)
    print('AUC:', auc)

    # Print ROC curve
    plt.plot(fpr, tpr, label='AUC -> %s (area = %0.2f)' % (met, auc))
    # plt.show()


def evaluate(G, dfnodes, graphEdges, method='jc', k=1):
    print('-' * 100)
    print('method: ', method)
    hop = 1 / k
    fold = k
    precisionSum = 0
    recallSum = 0
    temp1 = 0
    temp2 = hop
    iterNum = 1

    while temp2 <= 1:
        print('Iteration %i / %i :' % (iterNum, fold))
        iterNum += 1
        split_1 = int(temp1 * len(graphEdges))
        split_2 = int(temp2 * len(graphEdges))
        # print(split_1, split_2)
        # train_filenames = list(graphEdges)[split_1:split_2]
        test_filenames = list(graphEdges)[split_1: split_2]
        G2 = G.copy()
        G2.remove_edges_from(test_filenames)
        CG = nx.complement(G2)
        if method == 'jc':
            dictionary = jc_predict(G2, dfnodes)
        elif method == 'aa':
            dictionary = aa_predict(G2, dfnodes)
        elif method == 'cn':
            dictionary = cn_predict(G2, dfnodes)
        elif method == 'pa':
            dictionary = pa_predict(G2, dfnodes)
        else:
            raise Exception('Entered method is not valid', method)

        max = 0
        positive = []
        negative = []
        for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
            if max == 0:
                max = v
                trshold = 0.8 * max
            if v >= trshold:
                # print(k,v)
                positive.append(k)
                # else:
                #     negative.append(k)
        negative = (set(CG.edges) - set(positive))
        TP = set(positive).intersection(set(test_filenames))
        FN = set(negative).intersection(set(test_filenames))
        FP = []
        TN = set(negative) - set(FN)
        for i in positive:
            if not i in test_filenames:
                FP.append(i)

        precision = TP.__len__() / positive.__len__()
        recall = TP.__len__() / FN.__len__()
        precisionSum += precision
        recallSum += recall
        temp1 += hop
        temp2 += hop

    print("%i-fold evaluation precision: %f" % (fold, precisionSum / (fold)))
    print("%i-fold evaluation recall: %f" % (fold, recallSum / (fold)))

    # plt.show()
    print('-' * 100)


def evaluateROC(G, dfnodes, graphEdges, method='jc', k=10):
    print('-' * 100)
    print('method: ', method)
    fold = k
    hop = 1 / fold
    precisionSum = 0
    recallSum = 0
    temp1 = 0
    temp2 = hop

    iterNum = 1

    tprList = []
    fprList = []

    ''' |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| '''

    while temp2 <= 1:
        treshold = 0
        tresholdstep = fold
        print('(fold and treshold step) and (hop and ):', fold, hop)

        split_1 = int(temp1 * len(graphEdges))
        split_2 = int(temp2 * len(graphEdges))
        print(split_1, split_2)
        # train_filenames = list(graphEdges)[split_1:split_2]
        test_filenames = list(graphEdges)[split_1: split_2]
        G2 = G.copy()
        G2.remove_edges_from(test_filenames)
        print('g', G.edges.__len__())
        print('g2', G2.edges.__len__())
        # CG = nx.complement(G2)
        tpr_mean = []
        fpr_mean = []
        for i in range(tresholdstep + 1):
            if method == 'jc':
                dictionary = jc_predict(G2, dfnodes)
            elif method == 'aa':
                dictionary = aa_predict(G2, dfnodes)
            elif method == 'cn':
                dictionary = cn_predict(G2, dfnodes)
            elif method == 'pa':
                dictionary = pa_predict(G2, dfnodes)
            else:
                raise Exception('Entered method is not valid', method)

            max = 0
            positive = []
            negative = []
            for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
                if max == 0:
                    max = v
                    trshold = treshold * max
                else:
                    trshold = treshold * max

                if v >= trshold:
                    positive.append(k)
                else:
                    negative.append(k)

            # negative = (set(CG.edges) - set(positive))
            TP = set(positive).intersection(set(test_filenames))
            FN = set(negative).intersection(set(test_filenames))
            FP = []
            TN = set(negative) - set(FN)
            for j in positive:
                if not j in test_filenames:
                    FP.append(j)

            tpr_mean.append(TP.__len__() / (TP.__len__() + FN.__len__()))
            fpr_mean.append(FP.__len__() / (FP.__len__() + TN.__len__()))
            try:
                precision = TP.__len__() / (TP.__len__() + FP.__len__())
            except:
                precision = 0
            recall = TP.__len__() / (FN.__len__() + TP.__len__())
            # if treshold == 0.5:
            precisionSum += precision
            recallSum += recall
            treshold += 0.2
            treshold = round(treshold, 1)
            if precision == 1:
                print('tresh', treshold)
                print('tp', TP)
                print('fp', FP)
                print('t file names', test_filenames)

        tprList.append(tpr_mean)
        fprList.append(fpr_mean)
        temp1 += hop
        temp2 += hop

        # print("%i-fold evaluation precision: %f" % (fold, precisionSum / (fold)))
        # print("%i-fold evaluation recall: %f" % (fold, recallSum / (fold)))
    # print('precisionSum: ', precisionSum)
    precisionSum = precisionSum / (fold * tresholdstep)
    tprdic = {}
    fprdic = {}
    for s in range(tprList.__len__()):
        for k in range(tpr_mean.__len__()):
            if not k in tprdic.keys():
                tprdic.update({k: 0})
                tprdic[k] += tpr_mean[k]
            else:
                tprdic[k] += tpr_mean[k]
    for k2 in range(tpr_mean.__len__()):
        tprdic[k2] = tprdic[k2] / tprList.__len__()

    for s21 in range(fprList.__len__()):
        for k21 in range(fpr_mean.__len__()):
            if not k21 in fprdic.keys():
                fprdic.update({k21: 0})
                fprdic[k21] += fpr_mean[k21]
            else:
                fprdic[k21] += fpr_mean[k21]
    for k22 in range(fpr_mean.__len__()):
        fprdic[k22] = fprdic[k22] / fprList.__len__()

    return list(fprdic.values()), list(tprdic.values()), precisionSum
