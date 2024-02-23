from distribuciones import E,N
from reparaciones import Multiples_Simulaciones

"""
Sea T el tiempo estimado que tendra el sistema para dejar de funcionar.
Luego T=k*E(F) donde E(F) es el tiempo estimado que le tomara romperse 
a una maquina, mientras que k es el numero de maquinas que al romperse haran que
el sistema colapse. Luego k esta acotado por la cantidad de reemplazos.
k=m+(T-E(F))/E(G), donde m es el numero inicial de maquinas a reemplazar y
E(G) es el tiempo esperado que le tome reparar la maquina al mecanico. T-E(F) es
el tiempo estimado de la duracion del proceso menos el tiempo que le tome romperse
a la primera maquina. Luego despejando k:

    T/E(F)=m+((T-E(F))/E(G)
    T*E(G) = m*E(F)*E(G) + T*E(F) - E(F)^2
    T=(m*E(G) - E(F)) * E(F) / (E(G) - E(F))

Aqui asumimos que E(G) es mayor que E(F), ya que de lo contrario el valor esperado
seria potencialmente infinito.

Si m=10, E(G)=5 y E(F)=1 el tiempo esperado seria  T=(10*5 - 1) * 1/(5 - 1) = 12.25 unidades
de tiempo.
"""

def Estimate(F,G,M):
    return ((M*G)-F) * F / (G-F)

print("Introduzca el valor esperado para rotura de maquina")
F=int(input())
print("Introduzca el valor esperado para reparacion de maquina")
G=int(input())
print("Introduzca el numero de maquinas a reemplazar")
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
print("Media de los resultados obtenidos en simulaciones del primer modelo: "+str(Media))
print("Desviacion de los resultados obtenidos en simulaciones:"+str(Desvio))

print()

Eventos=Multiples_Simulaciones(lambda:E(F),lambda:N(G,G/10),numero_maquinas,M,10000,False)
Media=sum(Eventos)/len(Eventos)
Desvio=sum([abs(x-Media) for x in Eventos])/len(Eventos)
print("Media de los resultados obtenidos en simulaciones del segundo modelo: "+str(Media))
print("Desviacion de los resultados obtenidos en simulaciones:"+str(Desvio))


