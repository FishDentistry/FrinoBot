import requests
import json
import random 

cat_facts = []

def response():
    if len(cat_facts) == 0:
        r = requests.get('https://cat-fact.herokuapp.com/facts')
        data = r.json()
        for item in data['all']:
            cat_facts.append(item['text'])
        choice = random.randint(0,len(cat_facts)-1)
        msg = cat_facts[choice]
        return msg