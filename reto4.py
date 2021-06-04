"""
Created on Fri Jun  4 12:08:30 2021

@author: kevin
"""

import numpy as np

while True:
    n,m = input("Escriba: ").split()
    n = int(n)
    m = int(m)
    
    if n < 1:
        continue
    else:
        break

ciudades = []
cant_datos = []

for i in range(n):
    ciudades.append([])

for i in range(m):
    cant_datos.append(1)

datos = []

while len(datos) < len(cant_datos):
    x,y = input("Escriba 2: ").split()
    x = int(x)
    y = float(y)
    
    datos.append(x)
    
    if y > 605:
        continue
    else:
        ciudades[x-1].append(y)

ciudades_ica = []

for s in range(len(ciudades)):
    ciudades_ica.append([])
    for C in ciudades[s]:
        if 0 <= C < 55:
            II = 0
            IH = 50
            BPI = 0
            BPH = 54
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)

        elif 55 <= C < 155:
            II = 51
            IH = 100
            BPI = 55
            BPH = 154
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)

        elif 155 <= C < 255:
            II = 101
            IH = 150
            BPI = 155
            BPH = 254
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)

        elif 255 <= C < 355:
            II = 151
            IH = 200
            BPI = 255
            BPH = 354
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)

        elif 355 <= C < 425:
            II = 201
            IH = 300
            BPI = 355
            BPH = 424
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)

        elif 425 <= C < 505:
            II = 301
            IH = 400
            BPI = 425
            BPH = 504
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)
            
        elif 505 <= C < 605:
            II = 401
            IH = 500
            BPI = 505
            BPH = 604
            ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
            ciudades_ica[s].append(ICA)

j = 0

for k in ciudades_ica:
    if k == []:
        prom_ICA = 0
        mejor_ICA = 0
        peor_ICA = 0
        
    else:
        prom_ICA = np.mean(k)
        mejor = np.argmin(k)
        peor = np.argmax(k)
            
        mejor_ICA = ciudades_ica[j][mejor]
        peor_ICA = ciudades_ica[j][peor]
        
    verde = []
    amarillo = []
    naranja = []
    rojo = []
    morado = []
    marron = []
  
    for f in k:
        if 0 <= f <= 50:
                verde.append(f)
        elif 50 < f <= 100:
                amarillo.append(f)
        elif 100 < f  <= 150:
                naranja.append(f)
        elif 150 < f  <= 200:
                rojo.append(f)
        elif 200 < f  <= 300:
                morado.append(f)
        elif 300 < f :
                marron.append(f)
    
    menor_ICA = []
    igual_ICA = []
    mayor_ICA = []
    
    for m in k:
        if m < prom_ICA:
            menor_ICA.append(1)
        elif m == prom_ICA:
            igual_ICA.append(1)
        elif m > prom_ICA:
            mayor_ICA.append(1)
    
    j += 1
    
    print(j)
    print('%.2f' %mejor_ICA, '%.2f' %prom_ICA, '%.2f' %peor_ICA)
    print(len(verde),len(amarillo),len(naranja),len(rojo),len(morado),len(marron))
    print(len(menor_ICA),len(igual_ICA),len(mayor_ICA))


