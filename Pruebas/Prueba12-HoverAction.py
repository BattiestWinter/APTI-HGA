# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 12:47:57 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class using_unittest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Seleccionar un link text con la referencia del mouse
    def test_hover_action(self):
        url = 'https://www.google.com'
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        elem = driver.find_element(By.LINK_TEXT, 'Privacidad')
        # Movimiento del "mouse"
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(5)
        
    def tearDown(self):
        self.driver.close()
        

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()