import heapq
import distribuciones as d


distribuciones = [d.P,d.E,d.N,d.B,d.G,d.U,d.L,d.W]

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
        tiempo_para_reparar = roturas[0]
        while maquinas_a_reparar != 0 and tiempo_reparacion < tiempo_para_reparar:
            disponible += 1
            maquinas_a_reparar -= 1
            tiempo_para_reparar -= tiempo_reparacion
            tiempo_reparacion = G()

        if maquinas_a_reparar !=   0 and tiempo_reparacion > tiempo_para_reparar:
            tiempo_reparacion -= tiempo_para_reparar

        t += heapq.heappop(roturas)

        if disponible ==   0:
            break

        disponible -=   1
        maquinas_a_reparar +=   1
        heapq.heappush(roturas, t + F())

    return t


# Ejemplo de uso de la función reparar_maquinas

for i in distribuciones:
    for j in distribuciones:
        result = reparar_maquinas(i,j,5,3)
        print(f"Resultado de las distribuciones {i.__name__} y {j.__name__} : {result}")
    