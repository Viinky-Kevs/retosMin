import numpy

while True:
    data = str(input(": "))
    cant_1 = data.split()
    cant_c = int(cant_1[0])
    cant_d = int(cant_1[1])
    
    if cant_c < 1:
        continue
    else:
        break

lista_ciudades = []

for i in range(cant_c):
    lista_ciudades.append(i+1)

ciudades = [] 

for i in range(cant_c):
    ciudades.append([])

concentraciones = []

while len(concentraciones) < cant_d:
    data_2 = str(input(": "))
    data_3 = data_2.split()
    num_ciudad = int(data_3[0])
    concentracion = float(data_3[1])
    
    if num_ciudad in lista_ciudades:
        concentraciones.append(1)
        ciudades[num_ciudad-1].append(concentracion)
    else:
        continue

ICA_ciudades = []
    
for i in range(len(ciudades)):        
    ICA_ciudades.append([])
    for j in ciudades[i]:
        if 0 <= j < 55:
            II = 0
            IH = 50
            BPI = 0
            BPH = 54
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II  
            ICA_ciudades[i].append(ICA)
        elif 55 <= j < 155:
            II = 51
            IH = 100
            BPI = 55
            BPH = 154
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II
            ICA_ciudades[i].append(ICA)
                    
        elif 155 <= j < 255:
            II = 101
            IH = 150
            BPI = 155
            BPH = 254
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II
            ICA_ciudades[i].append(ICA)
                   
        elif 255 <= j < 355:
            II = 151
            IH = 200
            BPI = 255
            BPH = 354
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II
            ICA_ciudades[i].append(ICA)
                    
        elif 355 <= j < 425:
            II = 201
            IH = 300
            BPI = 355
            BPH = 424
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II
            ICA_ciudades[i].append(ICA)
                    
        elif 425 <= j < 505:
            II = 301
            IH = 400
            BPI = 425
            BPH = 504
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II
            ICA_ciudades[i].append(ICA)
                    
        elif 505 <= j < 605:
            II = 401
            IH = 500
            BPI = 505
            BPH = 604
            ICA = ((IH - II) / (BPH - BPI)) * (j - BPI) + II
            ICA_ciudades[i].append(ICA)

numero_ciudad = 0

for c in ICA_ciudades:
    
    if c == []:
        mejor_ICA = 0
        ICA_prom = 0
        peor_ICA = 0
    else:
        mejor_ICA = c[numpy.argmin(c)]
        ICA_prom = numpy.mean(c)
        peor_ICA = c[numpy.argmax(c)]
    
    verde = 0
    amarillo = 0
    naranja = 0
    rojo = 0
    morado = 0
    marron = 0
    
    menor_prom = 0
    igual_prom = 0
    mayor_prom = 0
    
    for k in c:
        if 0 <= k <= 50:
            verde += 1
        elif 50 < k  <= 100:
            amarillo += 1
        elif 100 < k  <= 150:
            naranja += 1
        elif 150 < k  <= 200:
            rojo += 1
        elif 200 < k  <= 300:
            morado += 1
        elif 300 < k:
            marron +=1
        
        if k < ICA_prom:
            menor_prom += 1
        elif k == ICA_prom:
            igual_prom += 1
        elif k > ICA_prom:
            mayor_prom += 1
        
    numero_ciudad += 1
    print(numero_ciudad)
    print('%.2f' %mejor_ICA, '%.2f' %ICA_prom , '%.2f' %peor_ICA)
    print(verde,amarillo,naranja,rojo,morado,marron)
    print(menor_prom, igual_prom, mayor_prom)
