from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

electros = ()
electros = list(electros)

# Electrodomesticos
electros.insert(-1, Electrodomestico(consumo="A", peso=15))

# Lavadoras
electros.insert(-1, Lavadora(consumo="E", peso=50, carga=30))

# Televisiones
electros.insert(-1, Television(peso=20, resolucion=30))


tv,lava,electro = 0,0,0
i = 0
for ele in electros:
    i+=1
    ele.precioFinal()

    if isinstance(ele,Television):
        tv += ele.precioBase
    elif isinstance(ele,Lavadora):
        lava += ele.precioBase
    else:
        electro += ele.precioBase

print("Televisiones: " + repr(tv))
print("Lavadoras: " + repr(lava))
print("Electrodomesticos varios: " + repr(electro))

print("Total: " + repr(tv+lava+electro))