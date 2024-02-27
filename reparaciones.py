import heapq

#Modelo 1 (Sin pérdida de memoria)
def reparar_maquinas(F, G, n, m):
    maquinas_a_reparar = 0
    roturas = []
    heapq.heapify(roturas)

    #Calcular el tiempo de rotura de las n máquinas
    for _ in range(n):
        heapq.heappush(roturas, F())

    t = 0
    disponible = m
    tiempo_reparacion = G() #Tiempo de reparación de la próxima máquina que se rompa
    tiempo_para_reparar = 0

    #Inicio de la simulación
    while True:
        tiempo_para_reparar = roturas[0]-t #Tiempo de la próxima que se romperá

        #Reparar máquinas rotas si las hay
        while maquinas_a_reparar != 0 and tiempo_reparacion < tiempo_para_reparar:
            disponible += 1
            maquinas_a_reparar -= 1
            tiempo_para_reparar -= tiempo_reparacion
            tiempo_reparacion = G()

        if maquinas_a_reparar != 0 and tiempo_reparacion > tiempo_para_reparar:
            tiempo_reparacion -= tiempo_para_reparar

        #Actualizar el tiempo
        t = heapq.heappop(roturas)

        #Comprobar que haya máquinas de respuesto
        if disponible == 0:
            break

        #Romper la próxima máquina y calcular el tiempo de duración del respuesto
        disponible -=   1
        maquinas_a_reparar +=   1
        heapq.heappush(roturas, t + F())

    return t



#Modelo 2(Con Pérdida de memoria)
def reparar_maquinas_V2(F, G, n, m):
    maquinas_a_reparar = 0
    t = 0
    disponible = m
    tiempo_reparacion = G() #Tiempo de reparación de la próxima máquina que se rompa

    #Inicio de simulación
    while True:
        tiempo_para_reparar = F() #Tiempo en que se romperá la próxima máquina
        t += tiempo_para_reparar #Actualizar el tiempo

        #Reparar máquinas rotas si las hay
        while maquinas_a_reparar != 0 and tiempo_reparacion < tiempo_para_reparar:
            disponible += 1
            maquinas_a_reparar -= 1
            tiempo_para_reparar -= tiempo_reparacion
            tiempo_reparacion = G()

        if maquinas_a_reparar != 0 and tiempo_reparacion > tiempo_para_reparar:
            tiempo_reparacion -= tiempo_para_reparar

        #Comprobar que haya máquinas de repuesto
        if disponible == 0:
            break

        disponible -= 1
        maquinas_a_reparar += 1
    return t


#Función para desarrollar varias simulaciones con los mismos parámetros
def Multiples_Simulaciones(F, G, n, m, Rep, Modelo):

    Resultados = []

    for _ in range(Rep):
        if Modelo == 2:
            Resultados.append(reparar_maquinas_V2(F, G, n, m))
        else:
            Resultados.append(reparar_maquinas(F, G, n, m))
    return Resultados
