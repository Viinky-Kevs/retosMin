# Reto 3
import numpy as np

cristian = True

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

promedios = []

for l in ciudades_ica:
    if l == []:
        promedios.append(0)
    else:
        prom = np.mean(l)
        promedios.append(prom)

valor_max = np.argmax(promedios)
valor_min = np.argmin(promedios)

v_promedio_min = promedios[valor_min]
v_promedio_max = promedios[valor_max]

verde = []
amarillo = []
naranja = []
rojo = []
morado = []
marron = []

for f in promedios:
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

prom_v = (len(verde)/len(promedios))*100
prom_a = (len(amarillo)/len(promedios))*100
prom_n = (len(naranja)/len(promedios))*100
prom_r = (len(rojo)/len(promedios))*100
prom_mo = (len(morado)/len(promedios))*100
prom_ma = (len(marron)/len(promedios))*100

if 0 <= v_promedio_min <= 50:
    alerta_min = "verde"
elif 50 < v_promedio_min  <= 100:
    alerta_min = "amarillo"
elif 100 < v_promedio_min  <= 150:
    alerta_min = "naranja"
elif 150 < v_promedio_min  <= 200:
    alerta_min = "rojo"
elif 200 < v_promedio_min  <= 300:
    alerta_min = "morado"
elif 300 < v_promedio_min :
    alerta_min = "marron"
        
if 0 <= v_promedio_max <= 50:
    alerta_max = "verde"
elif 50 < v_promedio_max  <= 100:
    alerta_max = "amarillo"
elif 100 < v_promedio_max  <= 150:
    alerta_max = "naranja"
elif 150 < v_promedio_max  <= 200:
    alerta_max = "rojo"
elif 200 < v_promedio_max  <= 300:
    alerta_max = "morado"
elif 300 < v_promedio_max :
    alerta_max = "marron"
    
print(valor_min + 1, "{:.2f}".format(promedios[valor_min]),alerta_min)
print(valor_max + 1, "{:.2f}".format(promedios[valor_max]),alerta_max)
print("verde", "{:.2f}%".format(prom_v))
print("amarillo", "{:.2f}%".format(prom_a))
print("naranja", "{:.2f}%".format(prom_n))
print("rojo", "{:.2f}%".format(prom_r))
print("morado", "{:.2f}%".format(prom_mo))
print("marron", "{:.2f}%".format(prom_ma))