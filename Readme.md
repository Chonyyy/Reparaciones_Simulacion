# Simulación de Reparaciones

### Autores:
> Javier Rodríguez Sánchez C-411

> María de Lourdes Choy Fernández C-412

> Luis Alejandro Rodríguez Otero C-411

## Breve introducción del proyecto ##

El proyecto consiste en analizar un problema de simulación de eventos discretos, implementar dicha simulación y analizar los resultados obtenidos por esta. El problema concreto consiste en un sistema que necesita n máquinas para funcionar y tiene m máquinas de respuesto, cada vez que una máquina se rompe es susutituida por una de las de respuesto y se envía a reparar, el tiempo de reparación y de duración de las máquinas siguen una distribución de variable aleatoria específica, el sistema falla cuando se rompe una máquina y no se cuenta con un reemplazo para esta.

## Objetivos y metas ##

El objetivo del proyecto es analizar distintos casos en los que llevar a cabo esta simulación, variar las distribuciones con que se rompen y se arreglan las máquinas, la cantidad de máquinas disponibles, asi como analizar la posibilidad de implementar más de un modelo que se ajuste al problema a simular. Principalmente el proyecto consiste en encontrar el o los escenarios en que el tiempo en que se rompe el sistema es mayor, es decir, que sea más duradero el sistema.

## Archivos ##

**distribuciones.py:** Distribuciones de variables aleatorias empleadas en la investigación

**reparaciones.py:** Implementación de los modelos de simulación

**Analisis de resultados.py:** Interfaz interactiva con la que introducir manualmente los parámetros de la simulación y visualizar los resultados de estas con ambos modelos, asi como el cálculo probabilístico.

**Imforme.tex/Informe.pdf:** Informe detallado sobre los resultados de la investigación, detalles de implementación, análisis, etc.