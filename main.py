# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from scrapper import Scrapper
import requests
import json

html = requests.get("https://pt.wikipedia.org/wiki/Lista_de_cursos_superiores_do_Brasil").content

scrapper = Scrapper()

result = scrapper.parse(html)

with open('output.json', 'w') as outfile:
    json.dump(result, outfile)