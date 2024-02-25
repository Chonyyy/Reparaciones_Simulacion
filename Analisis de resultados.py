from distribuciones import E,N
from reparaciones import Multiples_Simulaciones

# Estimación
def Estimate(F,G,M):
    return ((M*G)-F) * F / (G-F)

print("Introduzca el valor esperado para rotura de maquina")
F=int(input())
print("Introduzca el valor esperado para reparacion de maquina")
G=int(input())
print("Introduzca el numero de maquinas de reemplazo")
M=int(input())
print("Introduzca la cantidad de maquinas en el sistema")
numero_maquinas=int(input())
print("Tiempo esperado segun teoria: "  + str(Estimate(F,G,M)))

# Media de Simulaciones
Eventos=Multiples_Simulaciones(lambda:
                E(F),lambda:N(G,G/10),
                numero_maquinas,M,10000)
Media=sum(Eventos)/len(Eventos)
Desvio=sum([abs(x-Media) for x in Eventos])/len(Eventos)
print("Media de los resultados obtenidos en simulaciones del 2do modelo: "+str(Media))
print("Desviacion de los resultados obtenidos en simulaciones: "+str(Desvio))

print()

Eventos=Multiples_Simulaciones(lambda:E(F),lambda:N(G,G/10),numero_maquinas,M,10000,False)
Media=sum(Eventos)/len(Eventos)
Desvio=sum([abs(x-Media) for x in Eventos])/len(Eventos)
print("Media de los resultados obtenidos en simulaciones del 1er modelo: "+str(Media))
print("Desviacion de los resultados obtenidos en simulaciones: 5"+str(Desvio))