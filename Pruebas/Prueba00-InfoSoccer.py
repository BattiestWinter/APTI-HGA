# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:12:37 2022

@author: drago
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Web Driver como servicio
s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
browser = webdriver.Chrome(service = s)

# Link del sitio web
url = 'https://www.adamchoi.co.uk/teamgoals/detailed'
browser.get(url)

# Click en el botón "All matches" del sitio web
all_matches_button = browser.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

# Referencias claras en caso de no contar con elementos distinguibles como un ID
nReference = browser.find_element(By.CLASS_NAME, 'panel-body')

# Click en el selector de países del sitio web
dropdown = Select(nReference.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

# Tiempo implícito para no tener errores al momento de la extracción
time.sleep(5)

# Extraer valores dentro de una tabla
matches = browser.find_elements(By.TAG_NAME, 'tr')

# Extracción del texto de la lista matches
data = []
for match in matches:
    data.append(match.text)

# Cerrar el driver
browser.quit()

# Dataframe para guardar los datos en un archivo CSV
df = pd.DataFrame({'partidos':data})
print(df)
df.to_csv('partidos.csv', index=False) #Sólo los datos se pasan al archivo, no los índices
