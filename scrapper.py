# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class Scrapper():
    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        content_text = soup.find('div', class_='mw-parser-output')
        coursesName = set()

        for li_tag in content_text.select('ol > li > a'):
            name = li_tag.get_text().strip()
            if len(name) < 4 or name.startswith('de '):
                continue
            coursesName.add(name)

        courses = [{'id': i, 'name': course} for i, course in enumerate(sorted(coursesName))]
        return courses