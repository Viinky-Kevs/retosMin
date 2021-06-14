import numpy
import pandas
import statistics

info = pandas.read_csv("/home/kevin/Descargas/data.csv")

cristian = pandas.DataFrame(info)

entrada = input(": ").split()

lista_numeros = []

for i in entrada:
    numero = int(i)
    lista_numeros.append(numero)

lista_organizada = sorted(lista_numeros)

for c in lista_organizada:
    s_ciudad = cristian.loc[cristian["id_city"] == c]
    ciudad = s_ciudad["city_name"].iloc[0]
    departamento = s_ciudad["department_name"].iloc[0]
    measurement = s_ciudad["measurement"]
    
    nuevos_datos = []
    
    for i in measurement:
        nuevos_datos.append(i)
    
    count = len(s_ciudad)
    media_c = numpy.mean(measurement)
    desv_c = statistics.stdev(measurement)
    min_c = nuevos_datos[numpy.argmin(nuevos_datos)]
    max_c = nuevos_datos[numpy.argmax(nuevos_datos)]
    
    
    print(c, ciudad, departamento)
    print("count", count)
    print("c measurement")
    print("mean", '%.2f' %media_c)
    print("std", '%.2f' %desv_c)
    print("min", '%.2f' %min_c)
    print("max", '%.2f' %max_c)
    
    
    ICA_1 = []
    
    for e in nuevos_datos:
        if 0 <= e < 55:
            II = 0
            IH = 50
            BPI = 0
            BPH = 54
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)
                    
        elif 55 <= e < 155:
            II = 51
            IH = 100
            BPI = 55
            BPH = 154
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)
                    
        elif 155 <= e < 255:
            II = 101
            IH = 150
            BPI = 155
            BPH = 254
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)
                    
        elif 255 <= e < 355:
            II = 151
            IH = 200
            BPI = 255
            BPH = 354
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)
                    
        elif 355 <= e < 425:
            II = 201
            IH = 300
            BPI = 355
            BPH = 424
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)
                    
        elif 425 <= e < 505:
            II = 301
            IH = 400
            BPI = 425
            BPH = 504
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)
                    
        elif 505 <= e < 605:
            II = 401
            IH = 500
            BPI = 505
            BPH = 604
            ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
            ICA_1.append(ICA)   
    
    media_ica = numpy.mean(ICA_1)
    desv_ica = statistics.stdev(ICA_1)
    min_ica = ICA_1[numpy.argmin(ICA_1)]
    max_ica = ICA_1[numpy.argmax(ICA_1)]
    
    print("ica")   
    print("mean", '%.2f' %media_ica)
    print("std", '%.2f' %desv_ica)
    print("min", '%.2f' %min_ica)
    print("max", '%.2f' %max_ica)
    
    verde = 0
    amarillo = 0
    naranja = 0
    rojo = 0
    morado = 0
    marron = 0
    
    for j in ICA_1:
        if 0 <= j <= 50:
            verde += 1
        elif 50 < j  <= 100:
            amarillo +=1
        elif 100 < j  <= 150:
            naranja += 1
        elif 150 < j  <= 200:
            rojo += 1
        elif 200 < j  <= 300:
            morado += 1
        elif 300 < j :
            marron += 1
    
    print("alerts")
    print("verde", verde)
    print("amarillo", amarillo)
    print("naranja", naranja)
    print("rojo", rojo)
    print("morado", morado)
    print("marron", marron)




