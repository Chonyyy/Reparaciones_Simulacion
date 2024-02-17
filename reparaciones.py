import heapq

def F():
    # Implementación de la función F
    pass

def G():
    # Implementación de la función G
    pass

def reparar_maquinas(F, G, m, n):
    MaquinasAReparar =   0
    Roturas = []
    heapq.heapify(Roturas)

    for _ in range(m):
        heapq.heappush(Roturas, F())

    t =   0
    available = n
    Repairing_time = G()

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
tiempo_total = reparar_maquinas(F, G,  5,  3)
print(tiempo_total)