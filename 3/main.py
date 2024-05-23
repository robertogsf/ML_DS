# Importamos las bibliotecas necesarias
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Función para extraer el título del producto
def get_title(soup):
    try:
        # Buscamos el objeto de etiqueta externa
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Obtenemos el objeto NavigatableString interno
        title_value = title.text

        # Obtenemos el título como una cadena de texto
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Función para extraer el precio del producto
def get_price(soup):
    try:
        parent_span = soup.find("span", attrs={'class': 'a-price a-text-price a-size-medium apexPriceToPay'})
        child_aria_hidden = parent_span.find('span', {'aria-hidden': 'true'})
    
        if child_aria_hidden:
            price = child_aria_hidden.string.strip()
        else:
            # Si no se encuentra el span con aria-hidden='true', busca uno con la clase a-offscreen
            child_a_offscreen = parent_span.find('span', {'class': 'a-offscreen'})
            
            if child_a_offscreen:
                price = child_a_offscreen.string.strip()
    except AttributeError:
        try:
            # Si hay algún precio de oferta
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price

if __name__ == '__main__':
    # Añadimos nuestro user agent 
    HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})

    # La URL de la página web
    URL = "https://www.amazon.com/s?k=gaming+keyboard&language=es&_encoding=UTF8&content-id=amzn1.sym.8148f1e1-83ed-498f-85be-ff288b197da7&pd_rd_r=74fc56fd-8a17-460d-afac-d555b0c11ca6&pd_rd_w=Hpzsj&pd_rd_wg=V9jFi&pf_rd_p=8148f1e1-83ed-498f-85be-ff288b197da7&pf_rd_r=9XJABR50H9TFC5MFV28Z&ref=pd_hp_d_atf_unk"

    # Hacemos la solicitud HTTP
    webpage = requests.get(URL, headers=HEADERS)

    # Creamos el objeto Soup que contiene todos los datos
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Obtenemos los enlaces como una lista de objetos de etiquetas
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Almacenamos los enlaces
    links_list = []

    # Bucle para extraer los enlaces de los objetos de etiquetas
    for link in links:
            links_list.append(link.get('href'))

        # Creamos una lista para almacenar los productos
    products = []
    
    # Bucle para extraer los detalles del producto de cada enlace 
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Creamos un diccionario para almacenar los detalles del producto
        product = {}
        product['titulo'] = get_title(new_soup)
        product['precio'] = get_price(new_soup)

        # Añadimos el producto a la lista de productos
        products.append(product)

    # Creamos un DataFrame con los datos obtenidos
    amazon_df = pd.DataFrame(products)
    amazon_df['titulo'] = amazon_df['titulo'].replace('', np.nan)
    amazon_df = amazon_df.dropna(subset=['titulo'])

    # Guardamos los datos en un archivo JSON
    amazon_df.to_json("./3/amazon_products.json", orient='records', force_ascii=False)