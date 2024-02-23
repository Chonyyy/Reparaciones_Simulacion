import heapq
import scipy.stats as stats

def reparar_maquinas(F, G, m, n):
    maquinas_a_reparar =   0
    roturas = []
    heapq.heapify(roturas)

    for _ in range(m):
        heapq.heappush(roturas, F())

    t = 0
    disponible = n
    tiempo_reparacion = G()
    tiempo_para_reparar = 0

    while True:
        tiempo_para_reparar = roturas[0]-t
        while maquinas_a_reparar != 0 and tiempo_reparacion < tiempo_para_reparar:
            disponible += 1
            maquinas_a_reparar -= 1
            tiempo_para_reparar -= tiempo_reparacion
            tiempo_reparacion = G()

        if maquinas_a_reparar !=   0 and tiempo_reparacion > tiempo_para_reparar:
            tiempo_reparacion -= tiempo_para_reparar

        t = heapq.heappop(roturas)

        if disponible ==   0:
            break

        disponible -=   1
        maquinas_a_reparar +=   1
        heapq.heappush(roturas, t + F())

    return t

def reparar_maquinas_V2(F, G, m, n):
    maquinas_a_reparar =   0
    t = 0
    disponible = n
    tiempo_reparacion = G()

    while True:
        tiempo_para_reparar = F()
        t += tiempo_para_reparar
        while maquinas_a_reparar != 0 and tiempo_reparacion < tiempo_para_reparar:
            disponible += 1
            maquinas_a_reparar -= 1
            tiempo_para_reparar -= tiempo_reparacion
            tiempo_reparacion = G()

        if maquinas_a_reparar !=   0 and tiempo_reparacion > tiempo_para_reparar:
            tiempo_reparacion -= tiempo_para_reparar

        if disponible ==   0:
            break

        disponible -=   1
        maquinas_a_reparar +=   1
    return t

def Multiples_Simulaciones(F, G, m, n, Rep, V2=True):

    Resultados = []

    for _ in range(Rep):
        if V2:
            Resultados.append(reparar_maquinas_V2(F, G, m, n))
        else:
            Resultados.append(reparar_maquinas(F, G, m, n))
    return Resultados
