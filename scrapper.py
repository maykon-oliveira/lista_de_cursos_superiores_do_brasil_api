# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class Scrapper():
    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        content_text = soup.find('div', class_='mw-parser-output')
        courses = []

        for i, li_tag in enumerate(content_text.select('ol > li > a')):
            courses.append({'id': i, 'name': li_tag.get_text()})

        return courses