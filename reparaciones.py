import heapq
import distribuciones as d


distribuciones = [d.P,d.E,d.N,d.B,d.G,d.U,d.L,d.W]

def reparar_maquinas(F, G, m, n):
    MaquinasAReparar =   0
    Roturas = []
    heapq.heapify(Roturas)

    for _ in range(m):
        heapq.heappush(Roturas, F())

    t =   0
    available = n
    Repairing_time = G()
    time_to_repair =  0

    while True:
        if not Roturas:
            break

        time_for_repair = Roturas[0]
        while not MaquinasAReparar != 0 and Repairing_time < time_for_repair:
            available += 1
            MaquinasAReparar -= 1
            time_to_repair -= Repairing_time
            Repairing_time = G()

        if MaquinasAReparar !=   0 and Repairing_time > time_for_repair:
            Repairing_time -= time_for_repair

        t += heapq.heappop(Roturas)

        if available ==   0:
            break

        available -=   1
        MaquinasAReparar +=   1
        heapq.heappush(Roturas, F())

    return t


# Ejemplo de uso de la función reparar_maquinas

for i in distribuciones:
    for j in distribuciones:
        result = reparar_maquinas(i,j,5,3)
        print(f"Resultado de las distribuciones {i} y {j} : {result}")
    