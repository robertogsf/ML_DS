from bs4 import BeautifulSoup
from selenium import webdriver

# URL de la página web que quieres analizar
url = 'https://www.amazon.es/gp/bestsellers/?ref_=nav_cs_bestsellers'

# Crear el driver de Selenium (necesitarás tener el driver de Chrome descargado y en tu PATH)
driver = webdriver.Chrome()

# Cargar la página web
driver.get(url)

# Obtener el HTML de la página
html = driver.page_source

# Crear el objeto BeautifulSoup con el contenido de la página web
# Crear el objeto BeautifulSoup con el contenido de la página web
soup = BeautifulSoup(html, 'html.parser')

# Encontrar el elemento 'div' con id 'zg_left_colleft'
div = soup.find('div', class_='a-carousel-viewport')
print('Todos los productos',div)

# Encontrar todos los productos en el div
productos = div.find_all('div', {'data-asin': True})

# Lista para guardar los datos de los productos
datos_productos = []


# Iterar sobre cada producto
for producto in productos:
    # Extraer el título y el precio del producto
    titulo = producto.find('div', class_='p13n-sc-truncate-desktop-type2 p13n-sc-truncated').text.strip()
    precio = producto.find('span', class_='p13n-sc-price').text.strip()
    precio = precio.replace('\xa0', ' ')


    # Añadir los datos del producto a la lista
    datos_productos.append({
        'titulo': titulo,
        'precio': precio
    })

# Imprimir los datos de los productos
for producto in datos_productos:
    print(producto)
