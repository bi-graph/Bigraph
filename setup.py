from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if not l.startswith("#")]

    return requires


# requirements = parse_requirements_file("requirements_dev.txt")
requirements = ["networkx==2.5; python_version=='3.8'"]

setup(
    name="bigraph",
    version="0.2.12",
    author="Soran Ghadri",
    author_email="soran.gdr.cs@gmail.com",
    description="Link prediction in bipartite graphs",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/soran-ghadri/bigraph",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)