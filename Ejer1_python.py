# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:13:54 2025

@author: aitor
"""

import pandas as pd
import numpy as np
datos = pd.read_csv('ATP.csv', encoding='latin1')
print(datos)
print(datos.info())
print(datos.head())
nuevo= pd.DataFrame(datos)
nuevo= nuevo.replace(np.nan,"0")

print("********IMPRESIÓN CON NAN*********")
print(nuevo.info())

print("********ESTADÍSTICAS CON NAN*********")
print(nuevo.describe())

print("********ESTADÍSTICAS SOLAMENTE NÚMEROS*********")
print(nuevo.describe(include=[np.number]))

nuevo= nuevo.replace("N/A","0")
nuevo= nuevo.replace("N/A","0")

print("********ESTADÍSTICAS SIN N/A Y NR*********")
print(nuevo.describe())
print(list(nuevo))












