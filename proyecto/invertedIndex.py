# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernández
"""
import pandas as pd
import nltk
import os
import re
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import json

nltk.download('stopwords')

indice = []
dictionary = {}

# Directorio de trabajo
os.chdir('C:/Users/drago/Downloads/APTI-HGA/proyecto/baseDatos')
files_csv = os.listdir()

# Patrón para la tokenización del texto
pattern = r'''(?x)                 # set flag to allow verbose regexps
              (?:[A-Z]\.)+         # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*       # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
              | \.\.\.             # ellipsis
              | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
'''

# Palabras basura
stop_words = list(stopwords.words('spanish'))
new_stop_words = ['!', '()', '-', '[', ']', '{', '}', ';', ':', '"', '<>', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~', ',', '¿', '¡', 'nan', '(', ')']
for i in new_stop_words:
    stop_words.append(i)

df = pd.DataFrame()
for i in files_csv:
    
    
    # Formación del data frame a través de la lectura del archivo
    df = pd.read_csv(i)
    # print(df)
    
    # Contenido del campo text del data frame
    df_text = df['texto']
    
    # Conversión de los elementos del data frame a string para poder aplicar la función lower case
    df_text = [str(x) for x in df_text]
    df_text = [x.lower() for x in df_text]
    
    # Tokenización
    corpus = [nltk.regexp_tokenize(x, pattern) for x in df_text]
    # Adelgazamiento del corpus
    corpus_flatten = [x for iten in corpus for x in iten]
    
    # Limpieza de palabras basura
    clean_text = [x for x in corpus_flatten if x not in stop_words]
    
    # Frecuencia de palabras
    freq_new = list(FreqDist(clean_text).items())
    
    # Creación del diccionario (índice)
    for j in freq_new:
        # new_list = j.split(', ')
        # key = new_list[0]
        # value = new_list[1]
        
        # Separación de tupla generada al momento de obtener la frecuencia de palabras
        key, value = j
        
        # Definición de diccionario
        if key not in dictionary.keys():
            # dictionary.update({key: (value, i)})
            tmp_list = [(value, i)]
            dictionary[key] = tmp_list
        else:
            dictionary[key].append((value, i))
    
    #indice.append(list(freq_new.items()))
    
    # print("INDICE: ", indice)
    # indice.append(i)
    # indice.append(freq_new.items())

print(dictionary)
    
# print(indice[0])

# print("INDICE\n\n")
# print(indice[1])

tf = open("../diccionario.json", "w")
json.dump(dictionary, tf)
tf.close()
    