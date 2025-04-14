# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 19:34:20 2025

@author: aitor
"""

import pandas as pd
import numpy as np

datos= {'Nombres':['leonardo','Camilo', 'Jino','Tina'], 'Calificaciones': [
    '20','10','15','18'], 'Deportes': ['Fútbol', 'Tenis', 'Dormir','Basquet'],
    'Materias':['Lenguaje', 'Ética' , 'Educación Física', 'Matemáticas']}

df= pd.DataFrame(datos)
print("Esta es la table de la información de datos: ")
print(df)
print('\n'*4)


# DATOS NO VÁLIDOS
datos2= {'Nombres':['N/A','Camilo', 'Camilo','Tina'], 'Calificaciones': [
    '20','10',np.nan,'18'], 'Deportes': ['Fútbol', 'Tenis', 'Dormir','Basquet'],
    'Materias':['Lenguaje', 'Ética' , 'Educación Física', 'Matemáticas']}

df2= pd.DataFrame(datos2)
print(df2)
print('\n'*4)
print(df2.info())
print('\n'*4)
print(df2.describe())
print('\n'*4)
nuevo= pd.DataFrame(df2)
nuevo= nuevo.replace(np.nan,"0")
print(nuevo)
print('\n'*4)

#ELIMINAR REGISTRO BUSCANDO POR COLUMNA
columna= df2[df2['Nombres']!='N/A']
print(columna)
print('\n'*4)
df['Calificaciones']= df.Calificaciones.astype(int)
print(df.describe())









