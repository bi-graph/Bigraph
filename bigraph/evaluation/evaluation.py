from _operator import itemgetter

import numpy as np
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import KFold
from tabulate import tabulate

from bigraph import bigraph as pr
from bigraph.bigraph import jc_predict, aa_predict, cn_predict, pa_predict, katz_predict


def plot_ROC(fpr: list, tpr: list, met: str):
    """
    Plot ROC curve for algorithms
    :param fpr: *type: list - False positive rate metric
    :param tpr: *type: list - True positive rate metric
    :param met: Metric
    :return: True on success
    """
    # Print AUC
    auc = metrics.auc(fpr, tpr)
    # auc = np.trapz(tpr, fpr)
    print('AUC:', auc)
    # Print ROC curve
    plt.plot(fpr, tpr, label='AUC -> %s (area = %0.2f)' % (met, auc))
    # plt.show()
    return True


def _evaluate_method(G: object, k: int, method: str) -> list:
    """
    Evaluate algorithms using precision and AUC metrics
    :param G: Networkx bipartite graph
    :param k: Number of folds (used in KFold)
    :param method: Algorithm name
    :return: Calculated metrics: overal_precision, overal_auc, fpr_algo, tpr_algo
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
            predicted = jc_predict(G_train)
        elif method == 'aa':
            predicted = aa_predict(G_train)
        elif method == 'cn':
            predicted = cn_predict(G_train)
        elif method == 'pa':
            predicted = pa_predict(G_train)
        else:
            raise Exception('Entered method is not valid', method)
        # -------------------------------------------------------------------
        try:
            precision = len(set(predicted.keys()) & set(map(tuple, test_edges))) / len(set(predicted.keys()))
            print('precision: ', precision)
            precision_sum += precision
        except:
            print(f"{method} evaluation - Iterate {iterator}: Predicted 0 links")

        # -------------------------------------------------------------------
        fpr_algo = []
        tpr_algo = []
        try:
            score_algo, label_algo = zip(*[(float(score), label in test_edges) for label, score in
                                           sorted(predicted.items(), key=itemgetter(1), reverse=True)])
            # Compute the ROC AUC Score
            fpr_algo, tpr_algo, _ = roc_curve(label_algo, score_algo)
            auc_algo = roc_auc_score(label_algo, score_algo)
            print("auc: ", auc_algo)
            auc_sum += auc_algo
        except Exception as e:
            print(e)
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


def evaluate(G: object, k: int = 2, method: str = 'all'):
    """
    Evaluation interface for evaluating algorithms
    :param G: Networkx bipartite graph
    :param k: Number of folds (used in KFold)
    :param method: Algorithm name
    :return: Calculated metrics: overal_precision, overal_auc, fpr_algo, tpr_algo
    """
    methods = ['cn', 'jc', 'aa', 'pa']
    results = {}
    if method == 'all':
        for _method in methods:
            result = _evaluate_method(G, k, _method)
            results.update({method: result})
    elif method in methods:
        result = _evaluate_method(G, k, method)
        results.update({method: result})

    else:
        raise Exception('Make sure you have entered a valid method name.\n valid methods: all, cn, jc, aa, pa')
    return results


'''def evaluate(G, dfnodes, graphEdges, method, k):
    print('-' * 100)
    print('method: ', method)
    hop = 1 / k
    fold = k
    precisionSum = 0
    recallSum = 0
    temp1 = 0
    temp2 = hop
    iterNum = 1
    edges = G.edges
    print(list(edges))
    while temp2 <= 1:
        print('Iteration %i / %i :' % (iterNum, fold))
        iterNum += 1
        split_1 = int(temp1 * len(edges))
        split_2 = int(temp2 * len(edges))
        edge_subset = list(edges)[split_1: split_2]
        # ------------------------
        nodes_number = G.number_of_nodes()
        edges_number = G.number_of_edges()
        print("Number of nodes : %d" % nodes_number)
        print("Number of edges : %d" % edges_number)
        print("Number of connected components : %d" % nx.number_connected_components(G))
        # -------------------------
        G_train = G.copy()
        G_train.remove_edges_from(edge_subset)
        print(G['rs10183914'], G_train['rs10183914'])
        print("G_train in evaluation:\nnum of SNP: ", G_train.edges.__len__())
        edge_subset_size = len(list(edge_subset))
        print("Number of edges deleted : %d" % edge_subset_size)
        print("Number of edges remaining : %d" % (edges_number - edge_subset_size))
        # -------------------------

        # CG = nx.complement(G_train)
        if method == 'jc':
            predicted = pr.jc_predict(G_train, dfnodes)
        elif method == 'aa':
            predicted = pr.aa_predict(G_train, dfnodes)
        elif method == 'cn':
            predicted = pr.cn_predict(G_train, dfnodes)
        elif method == 'pa':
            predicted = pr.pa_predict(G_train, dfnodes)
        else:
            raise Exception('Entered method is not valid', method)

        pred_list = list(predicted)
        # print([(k in edge_subset) for (k, s) in sorted(predicted.items(), key=itemgetter(1), reverse=True)])
        # score_algo, label_algo = zip(*[(float(s), k in edge_subset) for k, s in sorted(predicted.items(), key=itemgetter(1), reverse=True)])
        print('edge_subset: ', edge_subset)
        # for k, v in sorted(predicted.items(), key=itemgetter(1), reverse=True):
        #     print(k)
        #     break
        # Compute the ROC AUC Score
        # print('score algo ', score_algo)
        # print('label algo ', label_algo)
        # fpr_algo, tpr_jaccard, _ = roc_curve(label_algo, score_algo)
        # auc_algo = roc_auc_score(label_algo, score_algo)
        # print("auc of the algorithm", auc_algo)
        # num = set(predicted.keys()) & set(edge_subset)
        print('==' * 100)
        # print(num.__len__(), num)
        # print('dic keys() ', set(predicted.keys()))
        # print('test_filelnames ', set(edge_subset))
        precisionSum += len(set(predicted.keys()) & set(edge_subset))/len(set(predicted.keys()))
        print('precision sum: ', precisionSum)
        print('---'*100)

        max = 0
        positive = []
        negative = []
        for k, v in sorted(predicted.items(), key=itemgetter(1), reverse=True):
            if max == 0:
                max = v
                trshold = 0.8 * max
            if v >= trshold:
                # print(k,v)
                positive.append(k)
                # else:
                #     negative.append(k)
        # negative = (set(CG.edges) - set(positive))
        TP = set(positive).intersection(set(edge_subset))
        # FN = set(negative).intersection(set(edge_subset))
        FP = []
        # TN = set(negative) - set(FN)
        for i in positive:
            if not i in edge_subset:
                FP.append(i)

        precision = TP.__len__() / positive.__len__()
        # recall = TP.__len__() / FN.__len__()
        precisionSum += precision
        # recallSum += recall
        temp1 += hop
        temp2 += hop

    print("%i-fold evaluation precision: %f" % (fold, precisionSum / (fold)))
    # print("%i-fold evaluation recall: %f" % (fold, recallSum / (fold)))

    # plt.show()
    print('-' * 100)'''

'''def evaluateROC(G, dfnodes, graphEdges, method='jc', k=10):
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


    while temp2 <= 1:
        treshold = 0
        tresholdstep = fold
        print('Iteration %i / %i :' % (iterNum, fold))
        print('(fold and treshold step) and (hop and ):', fold, hop)

        split_1 = int(temp1 * len(graphEdges))
        split_2 = int(temp2 * len(graphEdges))
        print(split_1, split_2)
        # train_filenames = list(graphEdges)[split_1:split_2]
        edge_subset = list(graphEdges)[split_1: split_2]
        G_train = G.copy()
        G_train.remove_edges_from(edge_subset)
        print('g', G.edges.__len__())
        print('G_train', G_train.edges.__len__())
        # CG = nx.complement(G_train)
        tpr_mean = []
        fpr_mean = []
        for i in range(tresholdstep + 1):
            if method == 'jc':
                predicted = pr.jc_predict(G_train, dfnodes)
            elif method == 'aa':
                predicted = pr.aa_predict(G_train, dfnodes)
            elif method == 'cn':
                predicted = pr.cn_predict(G_train, dfnodes)
            elif method == 'pa':
                predicted = pr.pa_predict(G_train, dfnodes)
            else:
                raise Exception('Entered method is not valid', method)

            max = 0
            positive = []
            negative = []
            for k, v in sorted(predicted.items(), key=itemgetter(1), reverse=True):
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
            TP = set(positive).intersection(set(edge_subset))
            FN = set(negative).intersection(set(edge_subset))
            FP = []
            TN = set(negative) - set(FN)
            for j in positive:
                if not j in edge_subset:
                    FP.append(j)

            tpr_mean.append(TP.__len__() / (TP.__len__() + FN.__len__()))
            fpr_mean.append(FP.__len__() / (FP.__len__() + TN.__len__()))
            try:
                precision = TP.__len__() / (TP.__len__() + FP.__len__())
            except:
                precision = 0
            recall = TP.__len__() / (FN.__len__() + TP.__len__())
            # if treshold == 0.5:
            print('mid pr: ', precision)
            precisionSum += precision
            recallSum += recall
            treshold += 0.2
            treshold = round(treshold, 1)
            if precision == 1:
                print('tresh', treshold)
                print('tp', TP)
                print('fp', FP)
                print('t file names', edge_subset)

        tprList.append(tpr_mean)
        fprList.append(fpr_mean)
        temp1 += hop
        temp2 += hop

        # print("%i-fold evaluation precision: %f" % (fold, precisionSum / (fold)))
        # print("%i-fold evaluation recall: %f" % (fold, recallSum / (fold)))
    # print('precisionSum: ', precisionSum)
    precisionSum = precisionSum / (fold * tresholdstep)
    print('-----pr:', precisionSum)
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

    return list(fprdic.values()), list(tprdic.values()), precisionSum'''''
