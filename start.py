from itertools import product
from urllib import response
import urllib.request 
import json

from db_helper import insert_product_to_db, initiaize_db
from product import Product
from sasto_pasal import SastoPasal


def fetch_product():
    url ="http://fakestoreapi.com/products"
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                    'Mozilla/5.0(Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
    response = urllib.request.urlopen(req)
    data = response.read()
    products = json.loads(data.decode('utf-8'))
    product_list =[]
    for product in products:
        product_list.append(
            Product(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
                image=product['image'],


            )
        )
    return product_list
    
if __name__ == "__main__":
    initiaize_db()
    product_list = fetch_product()
    insert_product_to_db(product_list=product_list)
    SastoPasal().take_order()

