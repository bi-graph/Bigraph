from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

name = "bigraph"
description = "Python package for link prediction in bipartite graphs and networks"

platforms = ["Linux", "Mac OSX", "Windows", "Unix"]

authors = {
    "Soran": ("Soran Ghadri", "soran.gdr.cs@gmail.com"),
    "Taleb": ("Taleb Zarhesh", "taleb.zarhesh@gmail.com"),
}

maintainer = "BiGraph Developers"
maintainer_email = "soran.gdr.cs@gmail.com"

keywords = [
    "Networks",
    "Graph Theory",
    "Mathematics",
    "network",
    "graph",
    "bipartite graph",
    "bigraph",
    "link prediction",
    "discrete mathematics",
    "math",
]

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Scientific/Engineering :: Physics",
]


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if not l.startswith("#")]

    return requires


extras_require = {
    dep: parse_requirements_file("requirements/" + dep + ".txt")
    for dep in ["developer", "doc", "extra", "test"]
}
requirements = parse_requirements_file("requirements/default.txt")
# requirements = ['networkx']


setup(
    name=name,
    version="0.1rc5",
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    author=authors["Soran"][0],
    author_email=authors["Soran"][1],
    description=description,
    long_description=readme,
    keywords=keywords,
    platforms=platforms,
    long_description_content_type="text/markdown",
    url="https://github.com/bi-graph/bigraph",
    packages=find_packages(),
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=classifiers,
    python_requires='>=3.6',
    zip_safe=False,
)
