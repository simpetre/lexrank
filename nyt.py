import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import time
API_KEY = '4e22eaec28a94fe8b99285a4029ef0a5'
import pickle

client = MongoClient()
db = client['newyorktimes_db']
tab = db['article_metadata']

def single_query(link, payload):
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING{}'.format(response.status_code))
        print(response.text)
        time.sleep(5)
    else:
        return response.json()

db.drop_collection('article_metadata')
tab = db['article_metadata']

if __name__ == '__main__':

    count = 1
    docs_list = []
    link = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
    end_date = '20170324'
    articles1 = []
    # while count < 120:
    #     payload = {'api-key': API_KEY, 'page': count, 'end_date' : end_date}
    #     html_str = single_query(link, payload)
    #     if html_str:
    #         for doc in html_str['response']['docs']:
    #             articles1.append(doc)
    #         #    if db.article_metadata.find({'_id': doc['_id']}).count() == 0:
    #         #        db.article_metadata.insert_one(doc)
    #         count += 1
    #         end_date = doc['pub_date'][:10].replace('-','')
    #         print(count)

    with open('urls.pkl', 'rb') as f:
        web_urls = pickle.load(f)

    article_texts = ["" for i in range(len(web_urls))]

    for i, url in enumerate(web_urls):
        response = requests.get(url)
        while response.status_code != 200:
            time.sleep(5)
            print(i)
            print('sleeping for five seconds...')
            response = requests.get(url)
        soup = BeautifulSoup(response.content)
        classes = soup.findAll('p', {'class': 'story-body-text story-content'})
        for cl in classes:
            article_texts[i] += cl.text
            article_texts[i] += '\n'
