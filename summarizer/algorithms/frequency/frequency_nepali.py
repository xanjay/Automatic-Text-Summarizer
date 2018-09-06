import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from heapq import nlargest
from collections import defaultdict

stopwords = set(stopwords.words('nepali') + list(punctuation))
min_cut = 0.1
max_cut = 0.9


def compute_frequencies(word_sent):
    """
    Compute the frequency of each word.
    Input: word_sent, a list of sentences already tokenized.
    Output:freq, a dictionary where freq[w] is the frequency of w.
    """
    freq = defaultdict(int)
    for s in word_sent:
        for word in s:
            if word not in stopwords:
                freq[word] += 1
    # frequencies normalization and filtering

    m = max(freq.values())
    for w in list(freq):
        freq[w] = freq[w] / m
        if freq[w] >= max_cut or freq[w] <= min_cut:
            del freq[w]
    return freq


def rank(ranking, n):
    """ Returns the first n sentences with highest ranking """
    return nlargest(n, ranking, key=ranking.get)


def nep_sent_tokenize(ntext):
    """"
    :param ntext: text to split into sentences
    :return: a tokenized sentences from the text
    """
    #return re.split(u'[।?!]', ntext)
    return re.split('(?<=[।?!]) +', ntext)


def frequency_main_nepali(text, sent_no):
    """
    Return a list of n sentences which is the summary of the text
    """
    result = []

    sents = nep_sent_tokenize(text)
    word_sent = [word_tokenize(s.lower()) for s in sents]

    freq = compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i, sent in enumerate(word_sent):
        for w in sent:
            if w in freq:
                ranking[i] += freq[w]
    sents_idx = rank(ranking, sent_no)
    [result.append(sents[j]) for j in sents_idx]
    return result
