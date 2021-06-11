"""
Created on Fri Jun 11 14:54:36 2021

@author: kevin
"""

import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")

cities = pd.DataFrame(data)

cities_in = input().split()
cities_in = sorted(cities_in)

entry_cities = []

for i in cities_in:
    num = int(i)
    entry_cities.append(num)

for i in entry_cities:
    select_city = cities.loc[cities["id_city"] == i]
    measurement = select_city["measurement"]
    city_name = select_city["city_name"]
    department_name = select_city["department_name"]
    
    print(i, city_name.iloc[0], department_name.iloc[0])
    print("count",len(select_city))
    
    c = []
    
    for j in measurement:
        c.append(j)
    
    mean_c = np.mean(c)
    std_c = np.std(c)
    minimum_c_1 = np.argmin(c)
    maximum_c_1 = np.argmax(c)
    
    minimum_c = c[minimum_c_1]
    maximum_c = c[maximum_c_1]
    
    print("c measurement")
    print("mean", '%.2f' %mean_c)
    print("std", '%.2f' %std_c)
    print("min", '%.2f' %minimum_c)
    print("max", '%.2f' %maximum_c)
    print("ica")
    
    ica = []
    verde = []
    amarillo = []
    naranja = []
    rojo = []
    morado = []
    marron = []
    
    for e in c:
            if 0 <= e < 55:
                II = 0
                IH = 50
                BPI = 0
                BPH = 54
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 0 <= ICA <= 50: ## Verde
                    ica.append(ICA)
                    verde.append(1)
                elif 50 < ICA <= 100: ## Amarillo
                    ica.append(ICA)
                    amarillo.append(1)
            elif 55 <= e < 155:
                II = 51
                IH = 100
                BPI = 55
                BPH = 154
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 50 < ICA <= 100: ## Amarillo
                    ica.append(ICA)
                    amarillo.append(1)
                elif 100 < ICA <= 150: ## Naranja
                    ica.append(ICA)
                    naranja.append(1)
            elif 155 <= e < 255:
                II = 101
                IH = 150
                BPI = 155
                BPH = 254
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 100 < ICA <= 150: ## Naranja
                    ica.append(ICA)
                    naranja.append(1)
                elif 150 < ICA <= 200: ## Rojo
                    ica.append(ICA)
                    rojo.append(1)
            elif 255 <= e < 355:
                II = 151
                IH = 200
                BPI = 255
                BPH = 354
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 150 < ICA <= 200: ## Rojo
                    ica.append(ICA)
                    rojo.append(1)
                elif 200 < ICA <= 300: ## Morado
                    ica.append(ICA)
                    morado.append(1)
            elif 355 <= e < 425:
                II = 201
                IH = 300
                BPI = 355
                BPH = 424
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 200 < ICA <= 300: ## Morado
                    ica.append(ICA)
                    morado.append(1)
                elif ICA > 300: ## Marrón
                    ica.append(ICA)
                    marron.append(1)
            elif 425 < e <= 505:
                II = 301
                IH = 400
                BPI = 425
                BPH = 504
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if ICA > 300: ## Marrón
                    ica.append(ICA)
                    marron.append(1)
            elif 505 <= e < 605:
                II = 401
                IH = 500
                BPI = 505
                BPH = 604
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if ICA > 300: ## Marrón
                    ica.append(ICA)
                    marron.append(1)
    
    mean_i = np.mean(ica)
    std_i = np.std(ica)
    minimum_i_1 = np.argmin(ica)
    maximum_i_1 = np.argmax(ica)
    
    minimum_i = ica[minimum_i_1]
    maximum_i = ica[maximum_i_1]
    
    print("mean", '%.2f' %mean_i)
    print("std", '%.2f' %std_i)
    print("min", '%.2f' %minimum_i)
    print("max", '%.2f' %maximum_i)
    print("alerts")
    print("verde", len(verde))
    print("amarillo", len(amarillo))
    print("naranja", len(naranja))
    print("rojo", len(rojo))
    print("morado", len(morado))
    print("marron", len(marron))