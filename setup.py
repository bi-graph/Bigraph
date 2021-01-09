from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["networkx==2.2"]

setup(
    name="bigraph",
    version="0.1.0",
    author="Soran Ghadri",
    author_email="jeffmshale@gmail.com",
    description="Link prediction in bipartite graphs",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/soran-ghadri/bigraph",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6+",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)