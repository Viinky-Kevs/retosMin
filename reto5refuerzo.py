"""
Created on Wed Jun 16 17:36:21 2021

@author: kevin
"""

import numpy as np
import pandas as pd
import statistics as sta
import math

data = pd.read_csv("data.csv")

cities = pd.DataFrame(data)

cities_in = input().split()

entry_cities = []

for i in cities_in:
    num = int(i)
    entry_cities.append(num)

sorted_entry = sorted(entry_cities)

for i in sorted_entry:
    select_c = cities.loc[cities["id_department"] == i]
    
    print(i, select_c["department_name"].iloc[0])
    print("terrain area")
    
    terrain = []
    for j in select_c["terrain_area"]:
        terrain.append(j)
    
    mean_t = np.mean(terrain)
    std_t = sta.stdev(terrain)
    min_t = terrain[np.argmin(terrain)]
    max_t = terrain[np.argmax(terrain)]
    total_t = sum(terrain)
    
    print("mean",'%.2f' %mean_t)
    print("std", '%.2f' %std_t)
    print("min", '%.2f' %min_t)
    print("max", '%.2f' %max_t)
    print("total", '%.2f' %total_t)
    
    print("old antenna")
    
    old = []
    for f in select_c["old_antenna"]:
        old.append(f)
    
    mean_o = np.mean(old)
    std_o = sta.stdev(old)
    min_o = old[np.argmin(old)]
    max_o = old[np.argmax(old)]
    total_o = sum(old)
    
    print("mean", '%.2f' %mean_o)
    print("std", '%.2f' %std_o)
    print("min", min_o)
    print("max", max_o)
    print("total", total_o)
    
    print("new antenna")
    
    a_1 = []
    b = []
    c = []
    d = []
    e = []
    ant_a = 4800
    
    new = []
    
    for a in select_c["new_antenna_type"]:
        new.append(a)
    
    for m in range(len(select_c)):
        l = new[m]
        area_p = ant_a * old[m]
        area_r = terrain[m] - area_p
        if old[m] >= 0:
            if l == "a":
                ant_final = area_r / 11400
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    a_1.append(ant)
            elif l == "b":
                ant_final = area_r / 12600
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    b.append(ant) 
            elif l == "c":
                ant_final = area_r / 41100
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    c.append(ant)
            elif l == "d":
                ant_final = area_r / 14700
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    d.append(ant)
            elif l == "e":
                ant_final = area_r / 38000
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    e.append(ant)
            else:
                continue
        else:
            continue
    print("a", sum(a_1))
    print("b", sum(b))
    print("c", sum(c))
    print("d", sum(d))
    print("e", sum(e))