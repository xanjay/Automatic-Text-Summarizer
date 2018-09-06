from pprint import pprint
import re
from bs4 import BeautifulSoup
import requests
from summarizer.algorithms.scoring import scoring_algorithm, scoring_nepali


def bbc_scraping():
    page = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(page.content, 'html.parser')
    newsDict = dict()
    div = soup.find('div', class_="nw-c-most-read__items gel-layout gel-layout--no-flex")
    newslist = div.find_all('div', class_="gs-o-media__body")  # find_all for all
    for i in range(5):
        news = newslist[i].a['href']
        news1 = 'https://www.bbc.com' + news
        page1 = requests.get(news1)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        heading = soup1.find('h1', class_='story-body__h1')
        body_div = soup1.find('div', class_='story-body__inner')
        body_paragraphs = body_div.find_all('p')
        body = ''
        for p in body_paragraphs:
            body = body + '\n' + p.get_text()
        result_list = scoring_algorithm.scoring_main(body, 5)
        summary = ' '.join(result_list)
        # pprint(body)
        newsDict[heading.get_text()] = summary
    return newsDict


def cnn_scraping():
    page = requests.get("http://rss.cnn.com/rss/edition.rss")
    soup = BeautifulSoup(page.content, features="xml")
    items = soup.find_all('item')
    newsDict = dict()
    titles = []
    links = []
    for i in items[:5]:
        titles.append(i.title.get_text())
        links.append(i.link.get_text())

    for count, l in enumerate(links):
        page1 = requests.get(l)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        pg = ''
        if re.match(r'^https://money.cnn', l) is not None:
            body_div_m = soup1.find('div', class_='storytext')
            body_p = body_div_m.find_all('p')
            for p in body_p:
                pg = pg + '\n' + p.get_text()
        else:
            body_div = soup1.find_all('div', class_='zn-body__paragraph')
            for div in body_div:
                pg = pg + '\n' + div.get_text()
        result_list = scoring_algorithm.scoring_main(pg, 5)
        summary = ' '.join(result_list)
        newsDict[titles[count]] = summary
    return newsDict


def nagarik_scraping():
    page = requests.get("https://nagariknews.nagariknetwork.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', class_="col-sm-4 title-second")
    links = div.find_all('a', class_=lambda x: x != "heading-link")
    newsDict = dict()
    titles = []
    body_links = []
    for i in range(5):
        titles.append(links[i].get_text())
        body_links.append('https://nagariknews.nagariknetwork.com' + links[i].get('href'))

    for count, l in enumerate(body_links):
        page1 = requests.get(l)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        div1 = soup1.find(id="newsContent")
        pgs = div1.find_all('p')
        body = ''
        for p in pgs:
            body = body + '\n\n' + p.get_text()
        result_list = scoring_nepali.scoring_main(body, 5)
        summary = ' '.join(result_list)
        newsDict[titles[count]] = summary
    return newsDict
