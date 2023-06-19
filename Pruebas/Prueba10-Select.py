# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:14:28 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class using_unittest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Seleccionar un valor de un Select Box
    def test_select(self):
        url = 'https://www.w3schools.com/howto/howto_custom_select.asp'
        driver = self.driver
        driver.get(url)
        sel = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/select')
        # Lista con las opciones disponibles
        options = sel.find_elements(By.TAG_NAME, 'option')
        time.sleep(3)
        # Recorrido con el valor de las opciones
        for i in options:
            print("Los valores son: %s" % i.get_attribute("value"))
            i.click()
            time.sleep(1)
        pick = Select(driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/select'))
        pick.select_by_value('10')
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()
        

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()