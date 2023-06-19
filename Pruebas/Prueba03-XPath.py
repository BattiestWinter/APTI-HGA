# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:25:56 2022

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

    """Uso de XPath"""    
    def test_search_by_xpath(self):
        url = 'https://google.com'
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        search_by_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        time.sleep(3)
        search_by_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)
    
    # Cierre del driver
    def tearDown(self):
        self.driver.close()
    
# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()
        
# Xpath es una estructura de objetos
# Xpath relativo: es más utilizado por los constantes cambios en el código, simplemente se señala el módulo específico del elemento
# Xpath absoluto: es menos utilizado por emplear toda la ruta, si la ruta se modifica afecta la búsqueda del elemento
        