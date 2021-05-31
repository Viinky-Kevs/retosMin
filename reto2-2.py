"""
Created on Mon May 31 11:19:32 2021

@author: kevin
"""

ICA = 51

cantidad = []
counter = 0
verde = []
amarillo = []
naranja = []
rojo = []
morado = []
marron = []

intervalo_1 = [0,50,0,54]
intervalo_2 = [51,100,55,154]
intervalo_3 = [101,150,155,254]
intervalo_4 = [151,200,255,354]
intervalo_5 = [201,300,355,424]
intervalo_6 = [301,400,425,504]
intervalo_7 = [401,500,505,604]
                    
def f_ica(intervalo):
    ICA = ((intervalo[1] - intervalo[0]) / (intervalo[3] - intervalo[2])) * (C - intervalo[2]) + intervalo[0]
    if 0 <= ICA <= 50:
        verde.append(1)
        cantidad.append(ICA)
        return(ICA)
    elif 50 < ICA <= 100:
        amarillo.append(1)
        cantidad.append(ICA)
        return(ICA)
    elif 100 < ICA <= 150:
        naranja.appenbd(1)
        cantidad.append(ICA)
        return(ICA)
    elif 150 < ICA <= 200:
        rojo.append(1)
        cantidad.append(ICA)
        return(ICA)
    elif 200 < ICA <= 300:
        morado.append(1)
        cantidad.append(ICA)
        return(ICA)
    elif ICA > 300:
        marron.append(1)
        cantidad.append(ICA)
        return(ICA)
    
while ICA > 50:
    C = float(input("Concentración: "))
    counter += 1
    if 0 <= C < 55:
        ICA = f_ica(intervalo_1)
    elif 55 <= C < 155:
        ICA = f_ica(intervalo_2)
    elif 155 <= C < 255:
        ICA = f_ica(intervalo_3)
    elif 255 <= C < 355:
        ICA = f_ica(intervalo_4)
    elif 355 <= C < 425:
        ICA = f_ica(intervalo_5)
    elif 425 <= C < 505:
        ICA = f_ica(intervalo_6)
    elif 505 <= C < 605:
        ICA = f_ica(intervalo_7)

promedio = sum(cantidad)/counter

if 0 <= promedio <= 50:
    alerta = "verde"
elif 50 < promedio <= 100:
    alerta = "amarillo"
elif 100 < promedio <= 150:
    alerta = "naranja"
elif 150 < promedio <= 200:
    alerta = "rojo"
elif 200 < promedio <= 300:
    alerta = "morado"
elif 300 < promedio:
    alerta = "marron"

p_verde = (len(verde) / counter) *100
p_amarillo = (len(amarillo) / counter) *100
p_naranja = (len(naranja) / counter) *100
p_rojo = (len(rojo) / counter) *100
p_morado = (len(morado) / counter) *100
p_marron = (len(marron) / counter) *100

print(counter)
print("{:.2f}".format(promedio), alerta)
print("verde", "{:.2f}%".format(p_verde))
print("amarillo", "{:.2f}%".format(p_amarillo))
print("naranja", "{:.2f}%".format(p_naranja))
print("rojo", "{:.2f}%".format(p_rojo))
print("morado", "{:.2f}%".format(p_morado))
print("marron", "{:.2f}%".format(p_marron))