# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:39:51 2025

@author: aitor
"""
import pandas as pd
datos = pd.read_csv('ATP.csv', encoding='latin1')
print(datos.info())
print(datos.head())
print(datos.iloc[0:5])
print(datos.iloc[[0,3,5,25],])

#COLUMNAS
print(datos.iloc[:, 0:2])
print(datos.iloc[[0,3,5,25],[0,5,6]])
print(datos.iloc[0:5, 5:8])