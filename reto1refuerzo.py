"""
Created on Sat Jun 12 11:18:59 2021

@author: kevin
"""
import math

area = float(input())
antenas = int(input())
tipo = str(input())

ant_a = 4800

letras = ["a","b","c","d","e"]

if antenas < 0:
    print("error en los datos")
else:
    area_p = ant_a * antenas
    area_r = area - area_p
    
    if tipo in letras:
        if tipo == "a":
            ant_final = area_r / 11400
        elif tipo == "b":
            ant_final = area_r / 12600
        elif tipo == "c":
            ant_final = area_r / 41100
        elif tipo == "d":
            ant_final = area_r / 14700
        elif tipo == "e":
            ant_final = area_r / 38000
        
        if ant_final < 0:
            print(0)
        else:
            print(math.ceil(ant_final))
    else:
        print("error en los datos")