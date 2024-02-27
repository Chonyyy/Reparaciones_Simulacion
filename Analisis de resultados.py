from distribuciones import E,N
from reparaciones import Multiples_Simulaciones

# Estimación
def Estimate(F,G,M):
    return ((M*G)-F) * F / (G-F)

print("Introduzca el valor esperado para rotura de maquina")
F=int(input())
print("Introduzca el valor esperado para reparacion de maquina")
G=int(input())
print("Introduzca la cantidad de maquinas en el sistema (n)")
n=int(input())
print("Introduzca la cantidad de maquinas de reemplazo (m)")
m=int(input())

print("Tiempo esperado segun estimación para Modelo 2: "  + str(Estimate(F,G,m)))


# Simulaciones en modelo 1
Eventos=Multiples_Simulaciones(lambda:E(F),lambda:N(G,G/10),n,m,10000, 1)
Media=sum(Eventos)/len(Eventos)
Desvio=sum([abs(x-Media) for x in Eventos])/len(Eventos)
print("Media de los resultados obtenidos en simulaciones del 1er modelo: "+str(Media))
print("Desviacion de los resultados obtenidos en simulaciones: "+str(Desvio))

print()

#Simulaciones en modelo 2
Eventos=Multiples_Simulaciones(lambda:E(F),lambda:N(G,G/10),n,m,10000, 2)
Media=sum(Eventos)/len(Eventos)
Desvio=sum([abs(x-Media) for x in Eventos])/len(Eventos)
print("Media de los resultados obtenidos en simulaciones del 2do modelo: "+str(Media))
print("Desviacion de los resultados obtenidos en simulaciones: "+str(Desvio))