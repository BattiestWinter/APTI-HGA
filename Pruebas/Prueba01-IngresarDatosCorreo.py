# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 12:58:18 2022

@author: drago
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Web Driver como servicio
s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service = s)

# Link del sitio web
url = 'https://www.gmail.com'
driver.get(url)

# Ingreso de correo en el sitio web
user = driver.find_element(By.ID, 'identifierId')
user.send_keys("spartanc932@gmail.com")
user.send_keys(Keys.ENTER)

# Tiempo implícito para no tener errores al momento de carga
time.sleep(5)

# Ingreso de contraseña en el sitio web
password = driver.find_element(By.NAME, 'password')
password.send_keys("123456")
password.send_keys(Keys.ENTER)
