# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernández
"""
import json
import pandas as pd
import os

tf = open("diccionario.json", "r")
dictionary = json.load(tf)

tf = open("municipios.json", "r")
municipios = json.load(tf)

years = []
for i in range(24):
    tmp = str(i)
    if len(tmp) == 1:
        year = '200' + tmp
    else:
        year = '20' + tmp
    years.append(year)

# print(years)

# print('MUNICIPIOS:')
# print(municipios)


query = input("Ingrese su busqueda: ")
# print(dictionary[query])

queries = query.split(" ")
print(queries)

suma = 0
count_years = 0
count_years_tmp = 0
df = pd.DataFrame()

for j in queries:
    mapData = {}
    mapData1 = []
    # mapData2 = []
    # count = 0
    # Bloque try-except para manejar el error KeyError
    try:
        if (dictionary[j]):   
            for i in dictionary[j]:
                # frecuencia, archivo = i
                frecuencia = i[0]
                archivo = i[1]
                searchTown = archivo.split("-")
                municipio = "NONE"
                anio = "NONE"
                newText =""
                
        
                # print("MUNICIPIO:\n")
                # print(township[searchTown[0]]) Primera parte del split
        
                os.chdir('C:/Users/drago/Downloads/APTI-HGA/proyecto/baseDatos')
                df = pd.read_csv(archivo)
                df_text = df['texto']
                # Conversión de los elementos del data frame a string para poder aplicar la función lower case
                df_text = [str(x) for x in df_text]
                df_text = [x.lower() for x in df_text]
        
                # Concatenación del texto
                for i in df_text:
                    newText += i + ' '
            
                # print(newText)
                # if('escuchar' in newText):
                    # print("ENCONTRADO")
        
                # Estructura para comparar la frecuencia de años
                for i in years:
                    count_years = 0
                    if (i in newText):
                        count_years += 1
                    if (count_years > count_years_tmp):
                        anio = i
                    count_years_tmp = count_years
        
                # munC = 0
                # Estructura para encontrar el municipio
                for i in municipios[(searchTown[0]).lower()]:
                    # munC += 1
                    if (i in newText):
                        municipio = i
                
                # Estructura para no repetir valores en la relación municipio-frecuencia
                if (municipio, anio) not in mapData.keys():
                    mapData[municipio, anio] = frecuencia
                else:
                    mapData[municipio, anio] += frecuencia
                # if municipio not in mapData.keys():
                #     mapData[municipio] = frecuencia
                # else:
                #     mapData[municipio] += frecuencia
                
                # Estructura para no repetir valores en la relación municipio-frecuencia NO APLICABLE
                # if count == 0:
                #     mapData1.append(municipio)
                #     mapData2.append(frecuencia)
                #     count += 1
                # else:
                #     if municipio == mapData1[count-1]:
                #         print("MUNICIPIO ACTUAL: %s" % municipio)
                #         print("MUNICIPIO ANTERIOR: %s" % mapData1[count-1])
                #         mapData2[count-1] += frecuencia
                #     else:
                #         mapData1.append(municipio)
                #         mapData2.append(frecuencia)
                #         count += 1
                    
                print('Archivo: %s' % archivo)
                print('Frecuencia: %i\nMunicipio: %s\nAño: %s\n' % (frecuencia, municipio, anio))
                suma += frecuencia
        
            print("Apariciones totales en el corpus de %s: %i" % (j, suma))
            print("\n")
    except Exception:
        print("palabra no encontrada")
    
    os.chdir('C:/Users/drago/Downloads/APTI-HGA/proyecto/baseDatosG')
    # Data Frame para cada búsqueda
    dfMap = pd.DataFrame({'municipio':mapData.keys(), 'frecuencia':mapData.values()})
    dfMap.to_csv('%s.csv' % j, index=False)
    

