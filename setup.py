from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Saketh\'s Artificially Intelligent Assistant'
LONG_DESCRIPTION = 'A package that performs simple tasks students would require.'

# Setting up
setup(
    name="saia",
    version=VERSION,
    author="SavvyHex (Saketh Pai)",
    author_email="<paisaketh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['periodictable'],
    keywords=['python', 'math', 'chemistry', 'elements', 'students', 'calculation'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)