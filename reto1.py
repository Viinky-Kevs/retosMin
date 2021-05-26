C = float(input("Ingrese la concentración PM:"))

if C>= 0 and C<55:
    II = 0
    IH = 50
    BPI = 0
    BPH = 54
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA>= 0 and ICA<=50:
        print("{:.2f}".format(ICA), "verde")
    elif ICA> 50 and ICA<=100:
        print('%.2f' %ICA, "amarillo")
    
elif C>= 55 and C<155:
    II = 51
    IH = 100
    BPI = 55
    BPH = 154
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA> 50 and ICA<=100:
        print('%.2f' %ICA, "amarillo")
    elif ICA> 100 and ICA<=150:
        print('%.2f' %ICA, "naranja")
        
elif C>= 155 and C<255:
    II = 101
    IH = 150
    BPI = 155
    BPH = 254
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA> 100 and ICA<=150:
        print('%.2f' %ICA, "naranja")
    elif ICA> 150 and ICA<=200:
        print(f'{ICA:.2f}', "rojo")
        
elif C>= 255 and C<355:
    II = 151
    IH = 200
    BPI = 255
    BPH = 354
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA> 150 and ICA<=200:
        print('%.2f' %ICA, "rojo")
    elif ICA> 200 and ICA<=300:
        print('%.2f' %ICA, "morado")
        
elif C>= 355 and C<425:
    II = 201
    IH = 300
    BPI = 355
    BPH = 424
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA> 200 and ICA<=300:
        print('%.2f' %ICA, "morado")
    elif ICA> 300:
        print('%.2f' %ICA, "marron")
        
elif C>= 425 and C<505:
    II = 301
    IH = 400
    BPI = 425
    BPH = 504
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA> 300:
        print('%.2f' %ICA, "marron")
elif C>= 505 and C<605:
    II = 401
    IH = 500
    BPI = 505
    BPH = 604
    ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
    if ICA> 300:
        print('%.2f' %ICA, "marron")
else:
    print("-1 error en los datos")