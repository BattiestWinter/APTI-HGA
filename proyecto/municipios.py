# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:39:36 2023

@author: drago
"""

import json
import pandas as pd
import os

os.chdir('C:/Users/drago/Downloads/APTI-HGA/proyecto/baseDatos')
dictionary = {}
count = 0
entidad_tmp = ""
inicio = 0

municipios = pd.DataFrame()

municipios = pd.read_csv("Municipios.csv")
entidad_texto = municipios[['entidad', 'municipio']]
# municipios_texto = municipios['municipio']
# entidad_texto = [str(x) for x in entidad_texto]
# municipios_texto = [str(x) for x in municipios_texto]
# entidad_texto = [x.lower() for x in entidad_texto]
# municipios_texto = [x.lower() for x in municipios_texto]
# print("MUNICIPIOS")
# print(municipios)
# print("\n")

lista_entidad = [x.lower() for x in list(entidad_texto['entidad'])]
lista_municipio = [x.lower() for x in list(entidad_texto['municipio'])]

# print(lista_entidad)
# print(len(lista_entidad))

for i in range(len(lista_entidad)):
    # Definición de diccionario
    if lista_entidad[i] not in dictionary.keys():
        dictionary[lista_entidad[i]] = [lista_municipio[i]]
    else:
        dictionary[lista_entidad[i]].append(lista_municipio[i])

print("DICCIONARIO: ")
print(dictionary)
    
tf = open("../municipios.json", "w")
json.dump(dictionary, tf)
tf.close()