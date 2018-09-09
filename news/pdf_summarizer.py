from pprint import pprint
from nltk import tokenize
import PyPDF2
from summarizer.algorithms.scoring import scoring_algorithm


def summarize_pdf(pdf_file, sent_percentage):
    pdf_file_obj = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    title = pdf_reader.getDocumentInfo().title
    summary_title = "Summary"
    if title is not None:
        summary_title = title+' - '+summary_title
    num_of_pages = pdf_reader.numPages
    body = ''
    for i in range(num_of_pages):
        pageobj = pdf_reader.getPage(i)
        body = body + "\n\n" + pageobj.extractText()

    pdf_file_obj.close()

    sentences = count_sent(body)
    sentence_no = int((sent_percentage / 100) * sentences)

    print(sentences)
    print(sentence_no)
    print('-------------------')

    result_list = scoring_algorithm.scoring_main(body, sentence_no)
    summary = "\r\n".join(result_list)  # \r only for display in notepad but \n is valid fro end-of-line
    summary = summary_title+"\r\n\r\n"+summary

    return summary


def count_sent(pdf_body):
    count = 0
    pags = pdf_body.split('\n\n')
    for p in pags:
        count = count+len(tokenize.sent_tokenize(p))

    return count


