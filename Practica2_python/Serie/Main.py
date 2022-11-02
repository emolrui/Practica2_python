from Videojuego import Videojuego
from Serie import Serie

series = list()
juegos = list()



series.insert(-1, Serie(titulo="Serie1",numTemporadas=1,entregado=True))
series.insert(-1, Serie(titulo="Serie2",numTemporadas=2,entregado=False))


juegos.insert(-1, Videojuego(titulo="Juego1", horasEstimadas=10,entregado=False))
juegos.insert(-1, Videojuego(titulo="Juego2", horasEstimadas=20,entregado=True))

serieMax = Serie()
juegoMax = Videojuego()

for i in series:
    if i.entregado:
        print(i)
        if i.numTemporadas > serieMax.numTemporadas:
            serieMax = i

for i in juegos:
    if i.entregado:
        print(i)
        if i.horasEstimadas > juegoMax.horasEstimadas:
            juegoMax=i

print("\nMayor: " + str(serieMax))
print("Mayor: " + str(juegoMax))