class ProductDetailMixin:

    def get_product_data(self,soup):
        block = soup.find('div',class_='product-details__row')
        rows = block.find_all('div',class_='params__row')
        characteristics = {
            row.find_all('div',class_='params__col')[0].get_text():
                row.find_all('div', class_='params__col')[1].get_text() for row in rows


        }
        return characteristics
