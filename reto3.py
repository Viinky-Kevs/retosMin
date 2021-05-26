def kevin():
    import numpy as np
    inicio = "inicio"
    # Primer ingreso n <- cantidad de ciudades
    #                m <- cantidad de datos
    while inicio != "ok":
        n, m = input(": ").split()
        n = int(n)
        m = int(m)
        
        if n < 1:
            continue
        else:
            inicio = "ok"
            
    cant_data = []
    for i in range(m):
        cant_data.append(i+1)
    
    cities = []
    for i in range(n):
        cities.append(i+1)
            
    cant_city = []
    for i in range(n):
        cant_city.append([])        
                
    data_raw = []
    
    # Segundo ingreso p <- número de ciudad
    #                 q <- concentración contaminante
    while len(data_raw) < len(cant_data):
        p, q = input(": ").split()
        p = int(p)
        q = float(q)
        
        if p not in cities:
            continue
        else:
            if q < 0 or q >= 605:
                continue
            else:
                data_raw.append(q)
                cant_city[p-1].append(q)
    
    # Tercer paso <- hallar ICA
    city_ica = []
    
    for r in range(len(cant_city)):
        city_ica.append([])
        for e in cant_city[r]:
            if 0 <= e < 55:
                II = 0
                IH = 50
                BPI = 0
                BPH = 54
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 0 <= ICA <= 50: ## Verde
                    city_ica[r].append(ICA)
                    
                elif 50 < ICA <= 100: ## Amarillo
                    city_ica[r].append(ICA)
                    
            elif 55 <= e < 155:
                II = 51
                IH = 100
                BPI = 55
                BPH = 154
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 50 < ICA <= 100: ## Amarillo
                    city_ica[r].append(ICA)
                    
                elif 100 < ICA <= 150: ## Naranja
                    city_ica[r].append(ICA)
                    
            elif 155 <= e < 255:
                II = 101
                IH = 150
                BPI = 155
                BPH = 254
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 100 < ICA <= 150: ## Naranja
                    city_ica[r].append(ICA)
                    
                elif 150 < ICA <= 200: ## Rojo
                    city_ica[r].append(ICA)
                    
            elif 255 <= e < 355:
                II = 151
                IH = 200
                BPI = 255
                BPH = 354
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 150 < ICA <= 200: ## Rojo
                    city_ica[r].append(ICA)
                    
                elif 200 < ICA <= 300: ## Morado
                    city_ica[r].append(ICA)
                    
            elif 355 <= e < 425:
                II = 201
                IH = 300
                BPI = 355
                BPH = 424
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if 200 < ICA <= 300: ## Morado
                    city_ica[r].append(ICA)
                    
                elif ICA > 300: ## Marrón
                    city_ica[r].append(ICA)
                    
            elif 425 < e <= 505:
                II = 301
                IH = 400
                BPI = 425
                BPH = 504
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if ICA > 300: ## Marrón
                    city_ica[r].append(ICA)
                    
            elif 505 <= e < 605:
                II = 401
                IH = 500
                BPI = 505
                BPH = 604
                ICA = ((IH - II) / (BPH - BPI)) * (e - BPI) + II
                if ICA > 300: ## Marrón
                    city_ica[r].append(ICA)
                    
    promedios = []
    
    for i in city_ica:
        if i == []:
            promedios.append(0)
        else: 
            promedio = np.mean(i)
            promedios.append(promedio)
    
    promedio_min = np.argmin(promedios)
    promedio_max = np.argmax(promedios)
    
    v_promedio_min = promedios[promedio_min]
    v_promedio_max = promedios[promedio_max]
    
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
    
    verde = []
    amarillo = []
    naranja = []
    rojo = []
    morado = []
    marron = []
    
    for i in promedios:
        if 0 <= i <= 50:
            verde.append(1)
        elif 50 < i  <= 100:
            amarillo.append(1)
        elif 100 < i  <= 150:
            naranja.append(1)
        elif 150 < i  <= 200:
            rojo.append(1)
        elif 200 < i  <= 300:
            morado.append(1)
        elif 300 < i :
            marron.append(1)

    p_alerta_v = (len(verde) / len(promedios)) * 100
    p_alerta_a = (len(amarillo) / len(promedios)) * 100
    p_alerta_n = (len(naranja) / len(promedios)) * 100
    p_alerta_r = (len(rojo) / len(promedios)) * 100
    p_alerta_mo = (len(morado) / len(promedios)) * 100
    p_alerta_ma = (len(marron) / len(promedios)) * 100
    
    city_min = promedio_min + 1
    city_max = promedio_max + 1    
    
    # Salidas
    print(city_min,"{:.2f}".format(promedios[promedio_min]),alerta_min)
    print(city_max,"{:.2f}".format(promedios[promedio_max]),alerta_max)
    print("verde", "{:.2f}%".format(p_alerta_v))
    print("amarillo", "{:.2f}%".format(p_alerta_a))
    print("naranja", "{:.2f}%".format(p_alerta_n))
    print("rojo", "{:.2f}%".format(p_alerta_r))
    print("morado", "{:.2f}%".format(p_alerta_mo))
    print("marron", "{:.2f}%".format(p_alerta_ma))
    
kevin()