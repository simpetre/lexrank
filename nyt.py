import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import time
import pickle

def single_query(link, payload):
    """Query link once, with parameters in payload
    INPUT: link (string): url to query
    OUTPUT: response.json(): json file containing results
    """
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING{}'.format(response.status_code))
        print(response.text)
        time.sleep(5)
    else:
        return response.json()

def populate_nyt_url_list(api_key, end_date='20170502'):
    """Query the New York Times API to get the most recent article urls
    INPUT: api_key (string): NYT API key
    end_date (int): the date of the most recent article url to return formatted
    as yyyymmdd
    """
    count = 1
    link = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
    articles = []
    while count < 120:
        payload = {'api-key': API_KEY, 'page': count, 'end_date' : end_date}
        html_str = single_query(link, payload)
        if html_str:
            for doc in html_str['response']['docs']:
                articles.append(doc)
            count += 1
            end_date = doc['pub_date'][:10].replace('-','')
    return articles

def scrape_article_text(articles):
    """Scrape the (NYT) article bodies from the URLs in articles
    INPUT: articles (list of strings): urls to scrape from
    OUTPUT: article_texts (list of strings): article texts
    """
    article_texts = ['' for i in range(len(web_urls))]

    for i, url in enumerate(docs_list):
        response = requests.get(url)
        while response.status_code != 200:
            time.sleep(5)
            response = requests.get(url)
        soup = BeautifulSoup(response.content)
        classes = soup.findAll('p', {'class': 'story-body-text story-content'})
        for cl in classes:
            article_texts[i] += cl.text
            article_texts[i] += '\n'
    return article_texts

if __name__ == '__main__':
    docs_list = populate_nyt_url_list(api_key, '20170502')
