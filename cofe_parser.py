import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_cofe_list():
    html = get_html("https://shoko.ru/menu/kofe/")
    if html:
        soup = BeautifulSoup(html, 'html5lib')
        all_cofe_list = soup.findAll('div', class_='product-card__inner')
        result_cofe_list = []
        for item in all_cofe_list:
            image_link = 'https://shoko.ru' + item.find('img')['data-src']
            title = item.find('h4').text
            price = item.find('div', class_='price').text.split()[0]

            result_cofe_list.append({
                'title': title,
                'picture': image_link,
                'price': price,
            })

def get_product_list():
  html = get_html("https://shoko.ru/menu/sendvichi-i-omlety/")
    if html:
        soup = BeautifulSoup(html, 'html5lib')
        all_product_list = soup.findAll('div', class_='product-card__inner')
        result_product_list = []
        for item in all_cofe_list:
            image_link = 'https://shoko.ru' + item.find('img')['data-src']
            title = item.find('h4').text
            price = item.find('div', class_='price').text.split()[0]

            result_product_list.append({
                'title': title,
                'picture': image_link,
                'price': price,
            })

            
        return result_product_list

if __name__ == "__main__":
    kofe_list = get_cofe_list()
    product_list = get_product_list()
    print(kofe_list[-1],product_list[-1])