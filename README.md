# BSSDH_2023_workshop on Advanced Python techniques for text content analysis

Program - http://www.digitalhumanities.lv/bssdh/2023/lectures-and-workshops/

## Day 1 - 25.07.2023

On the first day, participants will be introduced to the fundamentals of text content analysis, focusing on techniques to preprocess and analyze textual data. The session will cover text cleaning, tokenization, stemming, and lemmatization using libraries such as Gensim and Pandas. Attendees will learn how to convert raw text into structured data, suitable for further analysis. The day will conclude with an introduction to text feature extraction methods, including Bag-of-Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF), to prepare participants for Day 2's machine learning applications.

### Prerequisites

Participants should have basic knowledge of Python.
Recommended experience includes primitive data types, conditionals, iteration, lists,tuples, dictionaries and sets.

Helpful but not required experience: Jupyter Notebooks including Google Colab.

## Hardware/Software requirements in the order of preference

1. **Visual Studio Code with Python extension, Python itself and installed git** - Preferred (used by Instructor)
2. Any computer with modern browser and ability to connect to Google Colab
3. PyCharm (includes Python and git support)
4. Your own custom Jupyter Notebooks setup with Python

## Setup

* git - issues with notebooks
* 
### Installling libraries

### Practice with virtual enviroments - venv

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
* Latvian language serviceand other

### Stopwords


### Gensim

### Bag of Words

### TF-IDF

* Scikit-Learn

## Day 2 - 26.07.2023

Building on Day 1's foundation, the second day will delve into advanced discourse analysis techniques and machine learning applications, utilizing Scikit-learn and Gensim. Participants will explore various algorithms for topic modeling, such as Latent Dirichlet Allocation (LDA), and sentiment analysis, including Naïve Bayes and Support Vector Machines (SVM). Attendees will learn how to evaluate and fine-tune their models for optimal performance. The workshop will culminate in the creation of interactive visualizations using the Plotly library, empowering participants to effectively communicate their findings and insights to a broader audience.

### Topic modeling with - LDA - Latent Dirichlet Allocation

* history of LDA
* running LDA using gensim
* pyLDAvis

### Sentiment Analysis
* heiristic based sentiment analysis
* ml based sentiment analysis

### Fine-Tuning

### Plotly Visualization

### Assignment

Students will start with a raw corpus file that they will have to clean, pre-process, analyze and provide some results including visualization.
