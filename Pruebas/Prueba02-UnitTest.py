# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:28:44 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Clase unittest
class using_unitTest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    """Busqueda del sitio web
    Caso de prueba"""
    def test_search(self):
        url = 'https://google.com'
        driver = self.driver
        driver.get(url)
        # Validación del titulo de la página
        self.assertIn("Google", driver.title)
        element = driver.find_element(By.NAME, 'q')
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        # Verificación del elemento en la página
        assert "No se encontró el elemento" not in driver.page_source
    
    # Cierre del driver
    def tearDown(self):
        self.driver.close()

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()