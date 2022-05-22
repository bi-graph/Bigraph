import bigraph


def main():
    """
    Link prediction on a bipartite network
    :return:
    """

    bg = bigraph.BiGraph()

    bg.cn_predict()
    bg.jc_predict()
    bg.aa_predict()
    bg.pa_predict()


if __name__ == "__main__":
    main()
