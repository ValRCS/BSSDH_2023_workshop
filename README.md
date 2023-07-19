# BSSDH_2023_workshop on Advanced Python techniques for text content analysis

Program - http://www.digitalhumanities.lv/bssdh/2023/lectures-and-workshops/

## Day 1 - 25.07.2023

On the first day, participants will be introduced to the fundamentals of text content analysis, focusing on techniques to preprocess and analyze textual data. The session will cover text cleaning, tokenization, stemming, and lemmatization using libraries such as Gensim and Pandas. Attendees will learn how to convert raw text into structured data, suitable for further analysis. The day will conclude with an introduction to text feature extraction methods, including Bag-of-Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF), to prepare participants for Day 2's machine learning applications.

### Prerequisites

Participants should have basic knowledge of Python.
Recommended experience includes primitive data types, conditionals, iteration, lists, tuples, dictionaries and sets.

Helpful but not required experience: Jupyter Notebooks including Google Colab.

## Hardware/Software requirements in the order of preference

1. Easiest - Any computer with a modern browser and the ability to connect to Google Colab (requires google account - gmail)
2. **Visual Studio Code with Python extension, Python itself and installed git** - Preferred but not required(used by Instructor)
3. PyCharm (includes Python and git support)
4. Your own custom Jupyter Notebooks setup with Python

## Test minimal prerequisites

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ValRCS/BSSDH_2023_workshop/blob/main/notebooks/test_python_setup.ipynb)

<a target="_blank" href="https://colab.research.google.com/github/ValRCS/BSSDH_2023_workshop/blob/main/notebooks/test_python_setup.ipynb" rel="noopener"><img src="https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg" style="max-width: 100%;"></a>

If you can run the above Notebook in an environment of your choice (Google Colab, or locally) with no errors - you are ready for the workshop!




## Setup

* git installation - issues with notebooks
* 

### Practice with virtual environments - venv

**KEY idea** - Python virtual environments are light virtualization within OS - basically folders and symlinks (contrast with containerization using Docker and heavy virtualization with VirtualBox. VMware)
* https://docs.python.org/3/library/venv.html
* https://code.visualstudio.com/docs/python/environments
* Other IDEs such as PyCharm also offer virtual environment creation

* ### Installing libraries
* Installing external libraries on Colab
* Installing external libraries locally
* 
### Text Cleaning Techniques

### Normalization
* changing case
* removing symbols, accents
* Unicode normalization - https://unicode.org/reports/tr15/#Norm_Forms

## Pre-tokenization

### Tokenization
* whitespace
* word level
* sentence level
* BPE - byte pair level encoding - see https://huggingface.co/learn/nlp-course/chapter6/5?fw=pt
* Wordpiece tokenization - by Google similar to BPE

### Stemming vs Lemmatization

* https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html
* Caring -> car?!

### Stemming


### Lemmatization
* nltk
* Spacy
* Latvian language service and other

### Stopwords


### Gensim

### Bag of Words

### TF-IDF

* Scikit-Learn

## Day 2 - 26.07.2023

Building on Day 1's foundation, the second day will delve into advanced discourse analysis techniques and machine learning applications, utilizing Scikit-learn and Gensim. Participants will explore various algorithms for topic modeling, such as Latent Dirichlet Allocation (LDA), and sentiment analysis, including Naïve Bayes and Support Vector Machines (SVM). Attendees will learn how to evaluate and fine-tune their models for optimal performance. The workshop will culminate in creating interactive visualizations using the Plotly library, empowering participants to effectively communicate their findings and insights to a broader audience.

### Topic modeling with - LDA - Latent Dirichlet Allocation

* history of LDA
* running LDA using gensim
* pyLDAvis

### Sentiment Analysis
* heuristic based sentiment analysis
* ml-based sentiment analysis

### Fine-Tuning

### Plotly Visualization

### Assignment

Students will start with a raw corpus file that they will have to clean, pre-process, analyze and provide some results including visualization.
