ICA = 1000
cantidad = []
counter = 0
verde = []
amarillo = []
naranja = []
rojo = []
morado = []
marron = []

while ICA >50:
    C = float(input())
    
    counter += 1

    if C>= 0 and C<55:
        II = 0
        IH = 50
        BPI = 0
        BPH = 54
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA>= 0 and ICA<=50: ## Verde
            cantidad.append(ICA)
            count_verde = 1
            verde.append(count_verde)
        elif ICA> 50 and ICA<=100: ## Amarillo
            cantidad.append(ICA)
            count_amarillo = 1
            amarillo.append(count_amarillo)
        
    elif C>= 55 and C<155:
        II = 51
        IH = 100
        BPI = 55
        BPH = 154
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA> 50 and ICA<=100: ##Amarillo
            cantidad.append(ICA)
            count_amarillo = 1
            amarillo.append(count_amarillo)
        elif ICA> 100 and ICA<=150: ## Naranja
            cantidad.append(ICA)
            count_naranja = 1
            naranja.append(count_naranja)
            
    elif C>= 155 and C<255:
        II = 101
        IH = 150
        BPI = 155
        BPH = 254
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA> 100 and ICA<=150: ## Naranja
            cantidad.append(ICA)
            count_naranja = 1
            naranja.append(count_naranja)
        elif ICA> 150 and ICA<=200: ## Rojo
            cantidad.append(ICA)
            count_rojo = 1
            rojo.append(count_rojo)
            
    elif C>= 255 and C<355:
        II = 151
        IH = 200
        BPI = 255
        BPH = 354
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA> 150 and ICA<=200: ## Rojo
            cantidad.append(ICA)
            count_rojo = 1
            rojo.append(count_rojo)
        elif ICA> 200 and ICA<=300: ## Morado
            cantidad.append(ICA)
            count_morado = 1
            morado.append(count_morado)
            
    elif C>= 355 and C<425:
        II = 201
        IH = 300
        BPI = 355
        BPH = 424
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA> 200 and ICA<=300: ## Morado
            cantidad.append(ICA)
            count_morado = 1
            morado.append(count_morado)
        elif ICA> 300: ## Marron
            cantidad.append(ICA)
            count_marron = 1
            marron.append(count_marron)
            
    elif C>= 425 and C<505:
        II = 301
        IH = 400
        BPI = 425
        BPH = 504
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA> 300: ## Marron
            cantidad.append(ICA)
            count_marron = 1
            marron.append(count_marron)
            
    elif C>= 505 and C<605:
        II = 401
        IH = 500
        BPI = 505
        BPH = 604
        ICA = ((IH - II) / (BPH - BPI)) * (C - BPI) + II
        if ICA> 300: ## Marron
            cantidad.append(ICA)
            count_marron = 1
            marron.append(count_marron)

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











