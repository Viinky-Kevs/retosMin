"""
Created on Wed Jun 16 15:11:07 2021

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
a = []    
b = []
c = []
d = []
e = []

for i in range(n):
    depart.append([])
    id_depart.append(i+1)
    
    a.append([])
    b.append([])
    c.append([])
    d.append([])
    e.append([])

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
                    a[p-1].append(ant)
                    
            elif s == "b":
                ant_final = area_r / 12600
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
                    b[p-1].append(ant)
            elif s == "c":
                ant_final = area_r / 41100
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
                    c[p-1].append(ant)
            elif s == "d":
                ant_final = area_r / 14700
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
                    d[p-1].append(ant)
            elif s == "e":
                ant_final = area_r / 38000
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    depart[p-1].append(ant)
                    e[p-1].append(ant)
            else:
                depart[p-1].append(0)
        else:
            continue
    else:
        continue

for k in range(len(depart)):
    print(k+1)
    print(sum(depart[k]))
    
    letras = ["a", "b", "c", "d", "e"]
    
    datos_l = []
    
    datos_l.append(a[k])
    datos_l.append(b[k])
    datos_l.append(c[k])
    datos_l.append(d[k])
    datos_l.append(e[k])
    
    counter = 0
    for j in datos_l:
        if j == []:
            continue
        else:
            counter += 1
    
    if counter == 0:
        print("a", "0")
        print("a", "0")
    else:
        menor = datos_l[np.argmin(datos_l)]
        mayor = datos_l[np.argmax(datos_l)]
        letra_me = letras[np.argmin(datos_l)]
        letra_ma = letras[np.argmax(datos_l)]
        print(letra_me, sum(menor))
        print(letra_ma, sum(mayor))

letras = ["a", "b", "c", "d", "e"]


for m in range(len(letras)):
    
    if m == 0:
        datos_le = a
    elif m == 1:
        datos_le = b
    elif m == 2:
        datos_le = c
    elif m == 3:
        datos_le = d
    elif m == 4:
        datos_le = e
        
    counter = 0
    for z in datos_le:
        if z == []:
            continue
        else:
            counter += 1
    
    if counter == 0:
        print(1, letras[m],0)
        print(1, letras[m],0)
    else:
        menor = np.argmin(datos_le)
        mayor = np.argmax(datos_le)

        if len(datos_le) == 1:
            menor_ant = datos_le[0][menor]
            mayor_ant = datos_le[0][mayor]
            
            print(p, letras[m], menor_ant+mayor_ant)
            print(p, letras[m], menor_ant+mayor_ant)
            
        else:
            menor_ant = datos_le[menor]
            mayor_ant = datos_le[mayor]

            print(menor+1, letras[m], sum(menor_ant))
            print(mayor+1, letras[m], sum(mayor_ant))