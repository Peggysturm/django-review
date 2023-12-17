import requests
from bs4 import BeautifulSoup
from ..for_db.plumbing.models import Plumbing, PlumbingDetails
from django.template.defaultfilters import slugify


def parser(url: str, category, page):
    categories = {"all" : "https://smauro.ru/catalog/bytovaya_santekhnika/?PAGEN_2=", }
    base_url = "https://smauro.ru"
    if page == 0:
        page_url = categories[category] + str(1) 

    page_url = categories[category] + str(page)
    response = requests.get(url=page_url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="item")
    urls = []
    queryset = []
    raiting_list = []
    for product in products:
        name_elem = product.find("div", itemprop="name")
        link = name_elem.findNext().get("href")
        urls.append(base_url + link)
        raiting = int(product.find("li", class_="rcount").text)
        raiting_list.append(raiting)

    count = 0
    for url in urls:
        response = requests.get(url=url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        name = soup.select_one("h1").text
        try: 
            product = Plumbing.objects.get(name=name)
            queryset.append(product)
        except:
            price = soup.select_one("span.item_current_price").text
            description = soup.select_one("div.item_text").text
            product = Plumbing(name=name, slug=slugify(name+price), price=price, link=url)
            product.save()
            product_details = PlumbingDetails(plumbing=product, description=description, raiting=raiting_list[count])
            product_details.save()
            count += 1
            queryset.append(product)
            print(name)
    return queryset
    

if __name__ == "__main__":
    parser(url="https://smauro.ru/catalog/bytovaya_santekhnika/")