import requests
import re

def Create_Descriptions():
    my_API_key = '8a7e206944454a00a54918fd7a5ac7f7'
    headers = {'X-Api-Key': my_API_key}
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'source' : 'cnn',
        'language' :'en'

    }
    response = requests.get(url, headers=headers, params=params)
    articles =response.json()['articles']
    rev = []
    for article in articles:
        if article['description'] == None:
            continue
        tmplist = re.split('[ ,]',article['description'])
        tmp = (tmplist,article['url'])
        rev.append(tmp)
    return rev

def word_informations(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    response = requests.get(url+word)
    json_data = response.json()
    definition = ''
    syno = []
    anto = []
    if type(json_data) == list:
        data = (json_data[0]['meanings'][0]['definitions'][0]) 
        definition = data['definition']
        syno = data['synonyms']
        anto = data['antonyms']
        return definition,syno,anto
    else:
        return definition,syno,anto