import requests
from bs4 import BeautifulSoup


# def visible(element):
#     if element.parent.name in ['style', 'script', '[document]']:
#         return False
#     return True
#

def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_tag = list(filter(lambda p: len(list(p.children)) < 2, soup.find_all(['p', 'div'], class_=None, id=None)))
    text = ' '.join(map(lambda p: p.text, soup_tag))
    if text == '':
        text = 'No Paragraphs Found!'
    text = text.replace('\xa0', ' ')
    return text
