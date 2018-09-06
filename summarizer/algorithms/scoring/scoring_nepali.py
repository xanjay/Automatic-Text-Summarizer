from nltk.corpus import stopwords
from . import util, scoring_algorithm
from string import punctuation


def remove_stopwords(sentences):
    """
    Removes stopwords from the sentence
    :param sentences: (list) sentences
    :returns: cleaned sentences without any stopwords
    """
    sw = set(stopwords.words('nepali')+list(punctuation))
    cleaned = []
    for sentence in sentences:
        words = util.getWords(sentence)
        sentence = ' '.join([c for c in words if c not in sw])
        cleaned.append(sentence)
    return cleaned


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
            orig_sentences = util.getNepSentences(paragraph)
            sentences = remove_stopwords(orig_sentences)
            graph = scoring_algorithm.sentence_graph(sentences)
            score = scoring_algorithm.build(graph, orig_sentences)  # dictionary

        full_text.append(score)

    return util.sort_and_print(full_text, num)
