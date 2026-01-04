import requests
from bs4 import BeautifulSoup
import re

def obtener_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extraer_bloques(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select('.template-tlh__colors--hours')

def extraer_info_bloque(bloque):
    hora = bloque.select_one('.template-tlh__colors--hours-info span[itemprop="description"]')
    precio = bloque.select_one('.template-tlh__colors--hours-price span[itemprop="price"]')
    if hora and precio:
        hora_texto = hora.get_text(strip=True)
        precio_texto = precio.get_text(strip=True)
        match = re.search(r'([\d.,]+)', precio_texto)
        if match:
            precio_num = float(match.group(1).replace(',', '.'))
            return hora_texto, precio_num
    return None

def mostrar_resultados(resultados, precio_max):
    for hora, precio in resultados:
        etiqueta = "[ECO] " if precio <= precio_max else ""
        print(f"{etiqueta}{hora}: {precio:.3f} €/kWh")

def main():
    url = 'https://tarifaluzhora.es'
    precio_max = 0.135
    html = obtener_html(url)
    bloques = extraer_bloques(html)
    resultados = []
    for bloque in bloques:
        info = extraer_info_bloque(bloque)
        if info:
            resultados.append(info)
    mostrar_resultados(resultados, precio_max)

if __name__ == "__main__":
    main()

