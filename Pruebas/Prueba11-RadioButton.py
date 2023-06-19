# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 12:33:53 2022

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
    
    # Seleccionar un valor Radio Button
    def test_radio_button(self):
        url = 'https://www.w3schools.com/howto/howto_css_custom_checkbox.asp'
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        radio_bt = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/input[4]')
        radio_bt.click()
        time.sleep(3)
        radio_bt = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/input[3]')
        radio_bt.click()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()
        

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()