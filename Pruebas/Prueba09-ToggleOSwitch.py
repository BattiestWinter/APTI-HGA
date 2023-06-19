# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 10:54:57 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class using_unittest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Activar/Desactivar toggle
    def test_toggle(self):
        url = 'https://www.w3schools.com/howto/howto_css_switch.asp'
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        toggle = driver.find_element(By.XPATH, '//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)
    
    def tearDown(self):
        self.driver.close()
        

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()