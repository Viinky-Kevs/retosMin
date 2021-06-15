"""
Created on Tue Jun 15 14:58:59 2021

@author: kevin
"""

import numpy as np
import math

while True:
    entrada = input().split()
    n = int(entrada[0])
    m = int(entrada[1])
    
    if n < 1:
        continue
    else:
        break

depart = []
id_depart = []
ant_a = 4800

count_a = []

for i in range(n):
    depart.append([])
    id_depart.append(i+1)
    count_a.append([])
    
cant_data = []
while len(cant_data) < m:
    p,q,r,s = input().split()
    p = int(p)
    q = float(q)
    r = int(r)
    s = str(s)
    
    if p in id_depart:
        cant_data.append(1)
        area_p = ant_a * r
        area_r = q - area_p
        if r >= 0:
            if s == "a":
                ant_final = area_r / 11400
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
                    count_a[p-1].append(ant)
            elif s == "b":
                ant_final = area_r / 12600
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
            elif s == "c":
                ant_final = area_r / 41100
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
            elif s == "d":
                ant_final = area_r / 14700
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
            elif s == "e":
                ant_final = area_r / 38000
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
            else:
                depart[p-1].append(0)
        else:
            continue
    else:
        continue

antenas_f = []

for i in depart:
    suma = sum(i)
    antenas_f.append(suma)
        
valor_min = np.argmin(antenas_f)
valor_max = np.argmax(antenas_f)

menor = antenas_f[valor_min]
mayor = antenas_f[valor_max]

print(valor_min+1, menor)
print(valor_max+1, mayor)

for i in range(n):
    dep = sum(depart[i])
    if dep == 0:
        porc = 0
    else:
        porc = (sum(count_a[i]) / dep) * 100
    print(i+1, "{:.2f}%".format(porc))