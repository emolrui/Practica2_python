from Electrodomestico import Electrodomestico


class Television(Electrodomestico):
    def __init__(self, precioBase=150,color="negro",consumo='F',peso=5,resolucion=20,fourK=False):
        Electrodomestico.__init__(self, precioBase=precioBase,color=color,consumo=consumo,peso=peso)
        self.resolucion = resolucion
        self.fourK = fourK

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.resolucion > 40:
            self.precioBase = self.precioBase*1.3
        if self.fourK == True:
            self.precioBase = self.precioBase+50