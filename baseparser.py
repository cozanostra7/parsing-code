import requests
from bs4 import BeautifulSoup
import json
class BaseParser:
    def __init__(self):
        self.url = 'https://olcha.uz/ru'
        self.host = 'https://olcha.uz'


    def get_html(self,url= None):
        if url:
            html = requests.get(url).text
        else:
            html = requests.get(self.url).text
        return html

    def get_soup(self,html):
        return BeautifulSoup(html,'html.parser')

    @staticmethod
    def save_data_to_json(path,data):
        with open(path,mode='w',encoding = 'UTF-8') as file:
            json.dump (data,file,ensure_ascii=False,indent=4)

