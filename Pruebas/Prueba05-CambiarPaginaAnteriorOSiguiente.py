# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:34:50 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Cambiar entre página anterior y siguiente
    def test_next_or_previous_page(self):
        url = 'http://www.gmail.com'
        url1 = 'http://www.google.com'
        url2 = 'http://www.youtube.com'
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.get(url1)
        time.sleep(3)
        driver.get(url2)
        time.sleep(3)
        # Función para cambiar a la página anterior
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        # Función para cambiar a la página siguiente
        driver.forward()
        time.sleep(3)

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()
        
        