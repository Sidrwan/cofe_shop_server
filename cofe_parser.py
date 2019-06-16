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
        soup = BeautifulSoup(html, 'html.parser')
        all_cofe_list = soup.find(class="product-list line-3-in-row").findAll(class="title", class="price",'shoko.ru' + ["/upload/resize_cache/s1/fit_70_700x700/iblock/2f2/2f2ecd5dd54284e7b5bae80f22fb7d9e.jpg",
                                                                                                                "/upload/resize_cache/s1/fit_70_700x700/iblock/dc0/dc0f689a7bfd9d4b44ab963a7f940d2c.jpg",
                                                                                                                "/upload/resize_cache/s1/fit_70_700x700/iblock/290/290be3ac16503b65421e3277ca46ec21.jpg",
                                                                                                                '/upload/resize_cache/s1/fit_70_700x700/iblock/290/290be3ac16503b65421e3277ca46ec21.jpg"
                                                                                                                ])
        result_cofe_list = []
        for cofe_list in all_cofe_list:
            title = cofe.find(class="title").text
         #  picture = cofe.find(???).img     Пока непонятно как заполнять
            price = cofe.find(class="price").text
            result_cofe_list.append({
                'title': title,
                'picture': picture,
                'price': price,
            })
        return result_cofe_list
    return False
