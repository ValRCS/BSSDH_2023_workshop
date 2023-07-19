# Test your python setup by running this script 
# preferably you have activated your virtual environment first!
# without virtual enviroment this project will have to share libraries with other projects
# tests might take half a minute or so to run

from datetime import datetime
# print current date and time
print("Current date and time:", datetime.now())
# print python version
import sys
print("Python version", sys.version)
# for pandas I recommend installing the following
# from: https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies
# pip install "pandas[performance, plot, output_formatting, computation, excel, parquet, html, clipboard]"
# check pandas version
import pandas as pd
print("Pandas version", pd.__version__)
# check numpy version
import numpy as np
print("Numpy version", np.__version__)
# check requests version
import requests
print("Requests version", requests.__version__)
# check gensim version
import gensim
print("Gensim version", gensim.__version__)
# check scikit-learn version
import sklearn
print("Scikit-learn version", sklearn.__version__)
# check plotly version
import plotly
print("Plotly version", plotly.__version__)
# check spaCy version
import spacy
print("spaCy version", spacy.__version__)
# imports finished time
print("Imports finished at:", datetime.now())