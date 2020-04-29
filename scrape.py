import requests
import json
import re
import pandas as pd
import pprint
from bs4 import BeautifulSoup as bs
import bs4


if __name__ == "__main__":
    name = input('username: ') or 'ACRush'
    url = 'https://www.codechef.com/users/'+str(name)
    page = requests.get(url)
    soup = bs(page.text, 'lxml')
    cdata = str(soup.find(text=re.compile("CDATA")))
    temp = re.findall('"currentUser":".*","max',cdata)
    name = (soup.find('div', class_='user-details-container').header.h2.text)
    handle = json.loads('{'+temp[0][:-5]+'}')['currentUser']
    data = json.loads(re.findall('{"all.*\]}',cdata)[0])
    data = data['all']
    for entry in data:
        entry.update({'name': entry['name']+' ('+entry['code']+')'})
        entry.update({entry['name'] : entry['rank']})
        for key in ['color','getday','getmonth','getyear','penalised_in','reason','rating','end_date','code','name','rank']:
            entry.pop(key)

    pprint.pprint(data)


