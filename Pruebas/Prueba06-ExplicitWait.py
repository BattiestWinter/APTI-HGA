# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 01:08:00 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class using_unittest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Utilizar un tiempo de espera explícito
    def test_explicit_wait(self):
        url = 'http://google.com'
        driver = self.driver
        driver.get(url)
        try:
            # Intentar la carga del elemento 10 veces hasta que el elemento 'q' esté presente
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        finally:
            driver.quit()

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()


# Explicit Wait depende de las condiciones de carga, es decir, se necesita específicar algún 
# elemento que cargue para continuar con el proceso
            
        