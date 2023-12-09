import requests
from bs4 import BeautifulSoup
from .models import Plumbing, PlumbingDetails
from django.template.defaultfilters import slugify


def parser(url: str):
    base_url = "https://smauro.ru"
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="item")

    urls = []
    for product in products:
        name_elem = product.find("div", itemprop="name")
        link = name_elem.findNext().get("href")
        urls.append(base_url + link)

    for url in urls:
        response = requests.get(url=url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        name = soup.select_one("h1").text
        try: 
            product = Plumbing.objects.get(name=name)
        except:
            price = soup.select_one("span.item_current_price").text
            description = soup.select_one("div.item_text").text
            product = Plumbing(name=name, slug=slugify(name+price), price=price, link=url)
            product.save()
            product_details = PlumbingDetails(plumbing=product, description=description)
            product_details.save()
            print(name)
    

if __name__ == "__main__":
    parser(url="https://smauro.ru/catalog/bytovaya_santekhnika/")