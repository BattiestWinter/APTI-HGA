# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 03:52:15 2023

@author: drago
"""

# import geopandas as gpd
# import pandas as pd
# import matplotlib.pyplot as plt
# import json
# import os
# # Bokeh
# from bokeh.io import output_notebook, show, output_file, save
# from bokeh.plotting import figure
# from bokeh.models import GeoJSONDataSource, LinearColorMapper, HoverTool
# from bokeh.palettes import brewer
# import plotly as plt

# # %matplotlib inline

# # Importar polígonos de columnas
# shapfile = 'MEX_adm//MEX_adm2.shp'

# # Leer shapefile en geopandas
# gdf = gpd.read_file(shapfile, encoding='utf-8')[['ID_1','NAME_1','ID_2','NAME_2', 'geometry']]

# # Lectura del archivo csv con la frecuencia de palabra por municipio
# archivo_csv = pd.read_csv('baseDatosG/fosas.csv')

# # Filtración por estado
# for i in range(1,33):
#     try:
#         gdf = gdf[gdf['ID_1'] == i]
#         gdf['MUNICIPIO'] = gdf['NAME_2'].apply(lambda x: x.lower())
    
#         # Unión de ambos DataFrames
#         df_final = gdf.merge(archivo_csv, how = 'left', right_on = 'municipio', left_on = 'MUNICIPIO', suffixes = ("", "_2"))
    
#         # Renombramiento de columnas
#         df_final.rename(columns={'ID_1':'id_estado', 'NAME_1':'estado', 'ID_2':'id_municipio'}, inplace = True)

#         # DataFrame Final
#         df_final = df_final[['id_municipio', 'MUNICIPIO', 'frecuencia', 'geometry']]

#         df_final = df_final.fillna(0.1)
    
#         # Archivo json
#         archivo_json = json.loads(df_final.to_json())

#         # Conversión a string
#         json_data = json.dumps(archivo_json)
    
#         # Max color
#         max_color = df_final['frecuencia'].max()

#         # Carga de los datos: json_data
#         gsource = GeoJSONDataSource(geojson = json_data)

#         # Paleta de colores
#         colores = brewer['YlGnBu'][9]

#         # Reversión para que el número mayor sea más oscuro
#         colores = colores[::-1]

#         # Asociar un número a los colores: azul más alto, amarillo más bajo
#         color_mapper = LinearColorMapper(palette = colores, low = 0, high = max_color)

#         # Agregación de hovers
#         hover = HoverTool(names = ['Municipios'], tooltips = [('Municipio', '@MUNICIPIO'), ('Frecuencia', '@frecuencia')])

#         # Creación del objeto figura
#         fig = figure(title = 'Frecuencia por municipio',
#              plot_height = 600,
#              plot_width = 950,
#              toolbar_location = None,
#              tools = [hover])

#         # Detalles del canvas
#         fig.xgrid.grid_line_color = None
#         fig.ygrid.grid_line_color = None
#         fig.title.text_font_size = '20pt'

#         fig.axis.visible = False

#         # Mapeo | Dibujo de los polígonos
#         fig.patches('xs', 'ys',
#             source = gsource,
#             fill_color = {'field': 'frecuencia', 'transform': color_mapper},
#             line_color = 'black',
#             line_width = 0.25,
#             fill_alpha = 1,
#             name = 'Municipios')

#         # Archivo HTML
#         output_file('Mapas/Mapa_fosas_%i.html' % i)
#         save(fig)
    
#     except Exception:
#         print("No hay registros de frecuencias para el estado número %i" % i)

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
# Bokeh
from bokeh.io import output_notebook, show, output_file, save, export_png
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, HoverTool
from bokeh.palettes import brewer
import plotly as plt

# %matplotlib inline

# Importar polígonos de columnas
shapfile = 'MEX_adm//MEX_adm2.shp'

# Leer shapefile en geopandas
gdf = gpd.read_file(shapfile, encoding='utf-8')[['ID_1','NAME_1','ID_2','NAME_2', 'geometry']]

# Lectura del archivo csv con la frecuencia de palabra por municipio
archivo_csv = pd.read_csv('baseDatosG/cuerpos.csv')

archivo_csv['municipio'] = archivo_csv['municipio'].apply(lambda x: x.replace('(', ''))
archivo_csv['municipio'] = archivo_csv['municipio'].apply(lambda x: x.replace(')', ''))
archivo_csv['municipioD'] = archivo_csv['municipio'].apply(lambda x: x.replace("'", ''))
archivo_csv['municipio'] = archivo_csv['municipioD'].apply(lambda x: x.split(',')[0])
archivo_csv['anio'] = archivo_csv['municipioD'].apply(lambda x: x.split(',')[1])
archivo_csv['anio'] = archivo_csv['anio'].apply(lambda x: x.replace('NONE', '0'))
archivo_csv['anio'] = archivo_csv['anio'].apply(lambda x: int(x))

j = 2018

archivo_csv = archivo_csv[archivo_csv['anio'] == j]

# Filtración por estado
#for i in range(1,33):
i = 11
gdf = gdf[gdf['ID_1'] == i]
gdf['MUNICIPIO'] = gdf['NAME_2'].apply(lambda x: x.lower())

# Unión de ambos DataFrames
df_final = gdf.merge(archivo_csv, how = 'left', right_on = 'municipio', left_on = 'MUNICIPIO', suffixes = ("", "_2"))

# Renombramiento de columnas
df_final.rename(columns={'ID_1':'id_estado', 'NAME_1':'estado', 'ID_2':'id_municipio'}, inplace = True)

# DataFrame Final
df_final = df_final[['id_municipio', 'MUNICIPIO', 'frecuencia', 'geometry']]

df_final = df_final.fillna(0.1)

# Archivo json
archivo_json = json.loads(df_final.to_json())

# Conversión a string
json_data = json.dumps(archivo_json)

# Max color
max_color = df_final['frecuencia'].max()

# Carga de los datos: json_data
gsource = GeoJSONDataSource(geojson = json_data)

# Paleta de colores
colores = brewer['YlGnBu'][9]

# Reversión para que el número mayor sea más oscuro
colores = colores[::-1]

# Asociar un número a los colores: azul más alto, amarillo más bajo
color_mapper = LinearColorMapper(palette = colores, low = 0, high = max_color)

# Agregación de hovers
hover = HoverTool(names = ['Municipios'], tooltips = [('Municipio', '@MUNICIPIO'), ('Frecuencia', '@frecuencia')])

fig = figure()

# Creación del objeto figura
fig = figure(title = 'Frecuencia por municipio %i' % j,
         plot_height = 600,
         plot_width = 950,
         toolbar_location = None,
         tools = [hover])

# Detalles del canvas
fig.xgrid.grid_line_color = None
fig.ygrid.grid_line_color = None
fig.title.text_font_size = '20pt'

fig.axis.visible = False

# Mapeo | Dibujo de los polígonos
fig.patches('xs', 'ys',
        source = gsource,
        fill_color = {'field': 'frecuencia', 'transform': color_mapper},
        line_color = 'black',
        line_width = 0.25,
        fill_alpha = 1,
        name = 'Municipios')

print("BANDERA %i" % i)

# Archivo HTML
output_file('Mapas/Mapa_fosas_%i.html' % i)
save(fig)

# save(fig, 'Mapas/Mapa_fosas_%i.html' % i)

#     tf = open('Mapas/Mapa_fosas_%i.html' % i, "w")
#     tf.write(fig)
#     tf.close()
    
    