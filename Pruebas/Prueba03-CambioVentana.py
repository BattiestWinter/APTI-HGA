# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:15:48 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Clase unittest
class using_unitTest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Caso de Prueba, cambiar entre pestañas
    def test_change_window(self):
        url = 'https://google.com'
        url2 = 'http://stackoverflow.com'
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        # Abrir una nueva pestaña
        driver.execute_script("window.open('');")
        time.sleep(3)
        # Cambiar a la nueva pestaña, en la posición 1 (comienza desde 0)
        driver.switch_to.window(driver.window_handles[1])
        # Cargar una página en la nueva pestaña ([1])
        driver.get(url2)
        time.sleep(3)
        # Cambiar a la primera pestaña, en la posición 0
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()