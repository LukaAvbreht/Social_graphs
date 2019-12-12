import xml.dom.minidom
import re
import nltk
import matplotlib.pylab as plt
import pandas as pd
import json
import os
import pickle
import math


def tokenExtractor(file):
    doc = xml.dom.minidom.parse(file)

    movieText = ""

    for item in doc.getElementsByTagName("s"):
        for child in item.childNodes:
            if child.nodeName == "#text" and len(re.findall("\w", child.nodeValue)) > 1:
                movieText += child.nodeValue

    movieText = re.sub("\n\s+", " ", movieText)
    movieText = re.sub("\n", "", movieText)

    pattern = r'''(?x)(?:[A-Z]\.)+ | \w+(?:-\w+)*  | '''
    tokens = nltk.regexp_tokenize(movieText, pattern)

    # Remove non alphanumericbetic characters
    tokens = [w for w in tokens if re.search(r'\w', w)]

    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [w for w in tokens if w.lower() not in stopwords]
    stopwords = nltk.corpus.stopwords.words('spanish')
    tokens = [w for w in tokens if w.lower() not in stopwords]
    stopwords = nltk.corpus.stopwords.words('french')
    tokens = [w for w in tokens if w.lower() not in stopwords]
    stopwords = nltk.corpus.stopwords.words('italian')
    tokens = [w for w in tokens if w.lower() not in stopwords]

    # Remove numbers
    tokens = [w for w in tokens if not re.search(r'\d', w)]

    # Lower case
    tokens = [t.lower() for t in tokens]
    tokens = [item for item in tokens if item.isalpha()]

    return tokens


def computeTF(nbWords, tokens):
    tfDict = {}
    tokenCount = len(tokens)
    for word, count in nbWords.items():
        tfDict[word] = count / float(tokenCount)

    return tfDict


def computeIDF(documents):
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)

    for document in documents:
        for word, val in document.items():
            if val > 0:
                if word in idfDict:
                    idfDict[word] += 1
                else:
                    idfDict[word] = 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))

    return idfDict


def getNbUniqueWord(word_list):
    nb_word = {}
    for word in word_list:
        if word in nb_word:
            nb_word[word] += 1
        else:
            nb_word[word] = 1

    return nb_word


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf


def lexical_diversity(text):
    if len(text) == 0:
        return 0
    else:
        return len(set(text)) / len(text)


def percentage(text, word):
    return 100 * text.count(word) / len(text)


def frequency_distributions(text, words_num=75):
    """
    Creates frequency distribution form text and returns words_num most commom words.
    """
    all_words = list(set(text))
    res = list()
    for word in all_words:
        res.append((text.count(word), word))

    res.sort(reverse=True)
    return res[:words_num]


def cumulative_frequency(text, words_num=75):
    all_words = list(set(text))
    res = list()
    for word in all_words:
        res.append((text.count(word), word))

    res.sort(reverse=True)
    rres = list()
    suma = 0
    for (i, word) in res:
        suma += i
        rres.append(suma)
    return rres[:words_num]