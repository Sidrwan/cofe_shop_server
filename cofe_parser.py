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
        all_cofe_list = soup.find('div', class_="product-card__inner")
        for item in all_cofe_list:
            a = 'https://shoko.ru' + item.find('img')['data_src']

        result_cofe_list = []
        for cofe_list in all_cofe_list:
            title = cofe.find('h4').text
            picture = cofe.find('dev').jpg
            price = cofe.find("text").text
            result_cofe_list.append({
                'title': title,
                'picture': picture,
                'price': price,
            })
        return result_cofe_list
    return False