"""
Script to score sentences to get summary
"""

from nltk.corpus import stopwords
from . import util


def score_sentences(sen1, sen2):
    """
    Compares two sentences, find intersection and scores them
    :param sen1: (str) sentence
    :param sen2: (str) sentence
    :returns: score
    """

    s1 = set(sen1.lower().split())
    s2 = set(sen2.lower().split())
    score = 0
    if s1 and s2:
        avg = len(s1) + len(s2) / 2.0
        score = len(s1.intersection(s2)) / avg
    return score


def remove_stopwords(sentences):
    """
    Removes stopwords from the sentence
    :param sentences: (list) sentences
    :returns: cleaned sentences without any stopwords
    """
    sw = set(stopwords.words('english'))
    cleaned = []
    for sentence in sentences:
        words = util.getWords(sentence)
        sentence = ' '.join([c for c in words if c not in sw])
        cleaned.append(sentence)
    return cleaned


def sentence_graph(sentences):
    """
    Creates all pair score graph of sentences
    :param sentences: (list) list of sentences
    :returns: graph containing of all pair of sentence scores
    """
    scoreGraph = []
    len_sen = len(sentences)
    for i in range(len_sen):
        weight = []
        for j in range(len_sen):
            sentenceScore = 0
            if i == j:
                continue
            else:
                sentenceScore = score_sentences(sentences[i], sentences[j])
            weight.append(sentenceScore)
        scoreGraph.append(weight)

    return scoreGraph


def build(scoreGraph, orig_sentences):
    """
    Builds the content summary based on the graph
    :param orig_sentences: (list) list of original sentences
    :param scoreGraph: (list) 2 dimensional list-graph of scores
    :returns: Aggregate score(dictionary) of each sentence in `sentences`
    """
    aggregateScore = dict()
    sen = 0
    for scores in scoreGraph:
        aggregate = 0
        for i in scores:
            aggregate += i
        aggregateScore[orig_sentences[sen]] = aggregate
        sen += 1
    return aggregateScore


def scoring_main(content, num):
    """
    Execution starts here.
    Input's the content to be summarized.
    """
    # content = raw_input('Content: ')

    paragraphs = util.getParagraphs(content)
    full_text = []
    score = dict()

    for paragraph in paragraphs:
        if paragraph:
            orig_sentences = util.getSentences(paragraph)
            sentences = remove_stopwords(orig_sentences)
            graph = sentence_graph(sentences)
            score = build(graph, orig_sentences)  # dictionary
        full_text.append(score)

    return util.sort_and_print(full_text, num)
