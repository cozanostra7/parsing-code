
from baseparser import BaseParser
from time import time
from mixsins import ProductDetailMixin

class SiteParser(BaseParser,ProductDetailMixin):
    def __init__(self):
        super(SiteParser,self).__init__()
        self.data = {}

    def get_data(self):
        '''Основная функция сбора данных'''
        url = 'https://olcha.uz/ru/category/televizory-audio-i-videotekhnika'
        soup = self.get_soup(self.get_html(url))
        block = soup.find('div',class_='subcategory-list')
        categories = block.find_all('a',class_='subcategory')
        for category in categories:
            category_title = category.get_text()
            print(category_title)
            category_link =self.host + category.get('href')
            print(category_link)
            self.data[category_title] = []
            category_page = self.get_html(category_link)
            self.product_list_page_parser(category_title,category_page,category_link)

    def product_list_page_parser(self,category_title,category_page,category_link):
        soup = self.get_soup(category_page)
        pagination = soup.find('div',class_='paginations')
        print(pagination)
        try:
            last_page = pagination.find_all('a')[-2].get_text()
        except:
            last_page = 1
        print(last_page)
        for i in range (1,int(last_page)+1):
            soup = self.get_soup(self.get_html(category_link + f'?page={i}'))
            block = soup.find('div',class_='all-products-catalog__content')
            products = block.find_all('div', class_='product-card')
            for product in products:
                product_title = product.find('div',class_='product-card__brand-name')
                print(product_title)
                product_price = product.find('div',class_= 'price__main').get_text()
                product_price = int(''.join([letter for letter in product_price if letter.isdigit()]))
                print(product_price)
                product_image_link = product.find('img').get('src')

                #product_image_link = base64.decodebytes(product_image_link)
                #print(product_image_link)
                product_link = self.host + product.find('a').get('href')
                print(product_link)
                product_soup = self.get_soup(self.get_html(product_link))
                characteristics = self.get_product_data(product_soup)
                print(characteristics)
                self.data[category_title].append ({
                    'product_title': product_title,
                    'product_price': product_price,
                    'product_link':product_link,
                    'characteristics': characteristics

                })

def start_parsing():
    start = time()
    print('Parsing is started')
    parser = SiteParser()
    parser.get_data()
    parser.save_data_to_json('olcha.json',parser.data)
    finish = time()
    print(f'Parser has been done in {finish - start} seconds')


start_parsing()

