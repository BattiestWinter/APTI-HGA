# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 01:27:31 2022

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
    
    # Utilizar un tiempo de espera implícito
    def test_explicit_wait(self):
        url = 'http://google.com'
        driver = self.driver
        driver.implicitly_wait(5) # segundos | Funciona más como un límite de tiempo, es decir, si el 
                                  # elemento se encuentra antes de los 5 segundos, no es necesario esperar
                                  # el resto del tiempo (rango de espera)
        driver.get(url)
        # Obtener componente dinámico. Se utliza por si el elemento tiene un cambio 
        # constante en sus propiedades, i.e. ID)
        myDynamicElement = driver.find_element(By.NAME, 'q')

# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()

# Implicit Wait es muy parecido al time.sleep(). Espera una sentencia o tiempo en específico