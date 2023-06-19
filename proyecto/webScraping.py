# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernández
"""
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

search = input("Búsqueda: ")
location = input("Ubicación: ")

# Definición del controlador
s = Service('C:/Users/drago/Downloads/APTI-HGA/chromedriver.exe')
driver = webdriver.Chrome(service = s)

# Link del sitio web
url = 'https://google.com'
driver.get(url)

# Búsqueda
search_by_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_by_xpath.send_keys(search, Keys.ENTER)

# Links
links = driver.find_elements(By.CLASS_NAME, "yuRUbf")

references = []
count = 0

# Referencias de las páginas
for reference in links:
    references.append(reference.find_element(By.TAG_NAME, 'a').get_attribute("href"))

print(references)

# keywordsE = True
# keywords = []

# Extracción y almacenamiento de datos de cada página
for page in references:
    try:
        # Link de la página
        driver.get(page)
        time.sleep(10)
    except TimeoutException:
        pass

    # Variables para tratar el contenido de la página
    tittle = "NONE"
    subtittle = "NONE"
    content = "NONE"
    # contentC = ""
    datum = []
    
    # Bloque try catch para tratar los elementos no encontrados
    try:
        tittle = (driver.find_element(By.TAG_NAME, "h1")).text
    except NoSuchElementException:
        subtittle = (driver.find_element(By.TAG_NAME, "h2")).text
    content = (driver.find_elements(By.TAG_NAME, "p"))
    
    # Tratamiento del contenido generado por una lista de elementos web
    for c in content:
        # contentC += c.text
        datum.append(c.text)
    
    # Dato con la información de cada página
    datum.append(tittle)
    datum.append(subtittle)
    # datum.append(contentC)
    print(datum)
    
    # Guardar los datos en un archivo CSV
    df = pd.DataFrame({'texto':datum})
    # print(df)
    df.to_csv('baseDatos/%s-archivo%i.csv' % (location, count), index=False) # Sólo los datos se almacenan, no los índices
    count += 1 # Contador de archivos

driver.quit()

