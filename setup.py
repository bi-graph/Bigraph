import io
import os
import sys

from setuptools import setup, find_packages, Command
from shutil import rmtree

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

here = os.path.abspath(os.path.dirname(__file__))

NAME = "bigraph"
DESCRIPTION = "Python package for link prediction in bipartite graphs and networks"

PLATFORMS = ["Linux", "Mac OSX", "Windows", "Unix"]
VERSION = "0.1rc7"
AUTHORS = {
    "Soran": ("Soran Ghadri", "soran.gdr.cs@gmail.com"),
    "Taleb": ("Taleb Zarhesh", "taleb.zarhesh@gmail.com"),
}

MAINTAINER = "BiGraph Developers"
MAINTAINER_EMAIL = "soran.gdr.cs@gmail.com"

KEYWORDS = [
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

CLASSIFIERS = [
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

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = readme


# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

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
    name=NAME,
    version=about['__version__'],
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    author=AUTHORS["Soran"][0],
    author_email=AUTHORS["Soran"][1],
    description=DESCRIPTION,
    long_description=readme,
    keywords=KEYWORDS,
    platforms=PLATFORMS,
    long_description_content_type="text/markdown",
    url="https://github.com/bi-graph/bigraph",
    packages=find_packages(exclude=('tests', 'docs', 'html', 'requirements')),
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=CLASSIFIERS,
    python_requires='>=3.6',
    zip_safe=False,
)


class UploadCommand(Command):
    """Support setup.py upload."""

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()