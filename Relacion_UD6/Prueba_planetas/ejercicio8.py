from Planeta import Planeta
from datetime import datetime
import statistics

planetas_trappist = [
    Planeta("TRAPPIST-1b", 0.85 * 5.972e24, 1.116 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1c", 1.38 * 5.972e24, 1.097 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1d", 0.388 * 5.972e24, 0.788 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1e", 0.692 * 5.972e24, 0.920 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1f", 1.04 * 5.972e24, 1.045 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1g", 1.32 * 5.972e24, 1.127 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1h", 0.326 * 5.972e24, 0.755 * 6.371e6, datetime(2017, 2, 22), [])
]

planetas = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna", 1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4, 1.0659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Jupiter", 1.898e27, 6.9911e7, datetime.min, [["Ganimedes", 2.634e6, 1.4819e23], ["Calisto", 2.410e6, 1.0759e23], ["Ío", 1.821e6, 8.9319e22], ["Europa", 1.560e6, 4.7998e22]]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [["Titán", 2.575e6, 1.3452e23], ["Rea", 1.527e6, 2.3166e21], ["Japeto", 1.470e6, 1.8056e21], ["Dione", 1.123e6, 1.0955e21]]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6, 3.527e21]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Tritón", 1.353e6, 2.14e22]]),
    Planeta("Plutón", 1.303e22, 1.1883e6, "1930-02-18", [["Caronte", 6.057e5, 1.586e21]])
]

# La masa media de los planetas del Sistema Solar vs la masa media de lo planetas de TRAPPIST-1
masaTotalSol = [planeta.masa for planeta in planetas]
masaTotalTrappist = [planeta.masa for planeta in planetas_trappist]
masaMediaSol = statistics.mean(masaTotalSol)
masaMediaTrappist = statistics.mean(masaTotalTrappist)

print(f"La masa media de los planetas del Sistema Solar es: {masaMediaSol}")
print(f"La masa media de los planetas Trappist es: {masaMediaTrappist}")
print()

# El planeta más denso de ambos sistemas
densidadMaxSol = max([planeta.get_densidad() for planeta in planetas])
for planeta in planetas:
    densidad = planeta.get_densidad()
    if densidad == densidadMaxSol:
        planetaDensoSol = planetas.index(planeta)

densidadMaxTrap = max([planeta.get_densidad() for planeta in planetas_trappist])
for planeta in planetas_trappist:
    densidad = planeta.get_densidad()
    if densidad == densidadMaxTrap:
        planetaDensoTrap = planetas_trappist.index(planeta)

if densidadMaxTrap > densidadMaxSol:
    print(planetas_trappist[planetaDensoTrap])
else:
    print(planetas[planetaDensoSol])
print()
# El planeta de TRAPPIST-1 cuya densidad más se parece a la de la Tierra
densidadesTrap = [planeta.get_densidad() for planeta in planetas_trappist]
diferencia = [abs(planeta - densidadMaxSol) for planeta in densidadesTrap]
print(diferencia)
diferenciaMin = diferencia.index(min(diferencia))
print(planetas_trappist[diferenciaMin])
print()

# Los planetas sin lunas de ambos sistemas
planetasSinLunas = []

for planeta in planetas:
    if len(planeta.lunas) == 0:
        planetasSinLunas.append(planeta.nombre)

for planeta in planetas_trappist:
    if len(planeta.lunas) == 0:
        planetasSinLunas.append(planeta.nombre)

print(planetasSinLunas)
