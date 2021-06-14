"""
Created on Mon Jun 14 14:44:02 2021

@author: kevin
"""

import math

entrada_1 = int(input())

if entrada_1 > 0:
    datos = []
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
    ant_a = 4800
    semi_total = []

    while len(datos) < entrada_1:
        area = float(input())
        antenas = int(input())
        tipo = str(input())

        datos.append(area)

        area_p = ant_a * antenas
        area_r = area - area_p
        if antenas >= 0:
            if tipo == "a":
                ant_final = area_r / 11400
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    a += ant
                    semi_total.append(ant)
            elif tipo == "b":
                ant_final = area_r / 12600
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    b += ant
                    semi_total.append(ant)
            elif tipo == "c":
                ant_final = area_r / 41100
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    c += ant
                    semi_total.append(ant)
            elif tipo == "d":
                ant_final = area_r / 14700
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    d += ant
                    semi_total.append(ant)
            elif tipo == "e":
                ant_final = area_r / 38000
                ant = math.ceil(ant_final)
                if ant < 0:
                    pass
                else:
                    e += ant
                    semi_total.append(ant)
        else:
            continue
    total = sum(semi_total)
    
    a_p = (a / total) * 100
    b_p = (b / total) * 100
    c_p = (c / total) * 100
    d_p = (d / total) * 100
    e_p = (e / total) * 100

else:
    a_p = 0
    b_p = 0
    c_p = 0
    d_p = 0
    e_p = 0
    total = 0
    
print(total)
print("a", "{:0.2f}%".format(a_p))    
print("b", "{:0.2f}%".format(b_p))
print("c", "{:0.2f}%".format(c_p))
print("d", "{:0.2f}%".format(d_p))
print("e", "{:0.2f}%".format(e_p))