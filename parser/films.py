from pprint import pprint

import requests
from bs4 import BeautifulSoup

class ParserFilms:

    __URL = 'https://rezka.ag/films/horror/'

    __HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

    @classmethod
    def get_html(cls, url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req

    @staticmethod
    def get_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        itams = soup.find_all('div', class_='b-content__inline_item')
        ujas = []
        for itam in itams:
            info = itam.find('div', class_='b-content__inline_item-link').find('div').string.split(', ')
            card = {
                'title': itam.find('div', class_='b-content__inline_item-link').find('a').string,
                'link': itam.find('div', class_='b-content__inline_item-link').find('a').get('href'),
                'date': info[0],
                'country': info[1],
                'genre': info[-1],

            }
            ujas.append(card)
        return ujas

    @classmethod
    def parser(cls):
        html = cls.get_html()
        if html.status_code == 200:
            anime = []
            for i in range(1, 2):
                html = cls.get_html(f"{cls.__URL}page/{i}/")
                current_page = cls.get_data(html.text)
                anime.extend(current_page)
            return anime
        else:
            raise Exception("Bad request!")