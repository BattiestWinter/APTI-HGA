# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 02:05:25 2022

@author: drago
"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import time

class using_unittest(unittest.TestCase):
    
    """Inicializar el driver
    Web Driver como servicio"""
    def setUp(self):
        s = Service('C:/Users/drago/OneDrive/Escritorio/ServicioSocial/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)
    
    # Utilizar un tiempo de espera implícito
    def test_opencv(self):
        url = 'http://google.com'
        driver = self.driver
        driver.get(url)
        # Captura de pantalla de la ventana actual
        driver.save_screenshot('imagen02.png')
        time.sleep(3)
        
    def test_compare_images(self):
        # Carga de imágenes
        img1 = cv2.imread('imagen01.png')
        img2 = cv2.imread('imagen02.png')
        
        # Comparación entre la primera y segunda imagen | Diferencia en valor absoluto
        difference = cv2.absdiff(img1, img2)
        # Escalación de grises (facilita la comparación)
        gray_image = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        # Colección de datos 
        # https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
        contours,_ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Lectura cíclica de las dos imágenes
        for i in contours:
            # Límite de escalación de grises
            if cv2.contourArea(i) >= 20:
                # Encontrar la diferencia
                position_x, position_y, width, height = cv2.boundingRect(i)
                # Dibujar la diferencia
                cv2.rectangle(img1,(position_x, position_y),(position_x+width, position_y+height),(0,0,255), 2)
        
        while(1):
            cv2.imshow('Image01', img1)
            cv2.imshow('Image02', img2)
            cv2.imshow('Detected Diferrences', difference)
            keyboard = cv2.waitKey(5) & 0xFF
            if keyboard == 27:
                break
        cv2.destroyAllWindows()
        
# Llamada a la función unittest
if __name__ == '__main__':
    unittest.main()