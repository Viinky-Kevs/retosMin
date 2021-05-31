"""
Created on Mon May 31 10:29:33 2021

@author: kevin
"""

C = float(input("Concentración: "))

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
        print("{:.2f}".format(ICA), "verde")
    elif 50 < ICA <= 100:
        print('%.2f' %ICA, "amarillo")
    elif 100 < ICA <= 150:
        print('%.2f' %ICA, "naranja")
    elif 150 < ICA <= 200:
        print(f'{ICA:.2f}', "rojo")
    elif 200 < ICA <= 300:
        print('%.2f' %ICA, "morado")
    elif ICA > 300:
        print('%.2f' %ICA, "marron")

if 0 <= C < 55:
    f_ica(intervalo_1)
elif 55 <= C < 155:
    f_ica(intervalo_2)
elif 155 <= C < 255:
    f_ica(intervalo_3)
elif 255 <= C < 355:
    f_ica(intervalo_4)
elif 355 <= C < 425:
    f_ica(intervalo_5)
elif 425 <= C < 505:
    f_ica(intervalo_6)
elif 505 <= C < 605:
    f_ica(intervalo_7)
else:
    print("-1 error en los datos")