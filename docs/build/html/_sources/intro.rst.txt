Introduction
============

``bigraph`` is a high-level OO Python package which aims to provide an easy and intuitive way of interacting with bipartite networks. In essence, this package is an extension of the ``NetworkX`` package (see `here <https://github.com/networkx/networkx/>`_)

The aim here was to define an easy-to-use package which would allow developers to perform ``link pridiction``, ``evaluation``, and ``visualization`` of the results. 

The current implementation has been developed and tested in Python 3.6+, but should work with Python 2.7+ (maybe with minor modifications in terms of printing and error handling) and most Debian based OSs.

Motivation
**********

As a developer in the field of machine learning, I found it pretty hard to identify a Python package which would enable one to perform link pridiction algorithms over bipartite networks.

This package is intended to provide a quick, as well as (hopefully) easy to undestand, way of dealing-with-bipartite-networks algorithm up and running, for all those out there, who, like myself, are hands-on learners and are eager to get their hands dirty from early on.

Limitations
***********

- Algorithms are quite a few, and thus have to be piled with new ones.
- Evaluations used here are techniques used for unsupervised methods, however they may have to be modified.
- There are more limitations for sure if you happened to encounter any issue, you are welcomed to make contributions or open and issue on github.