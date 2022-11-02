class Electrodomestico:
    def __init__(self, precioBase=100,color="azul",consumo='F',peso=5):
        if color in ("blanco", "negro", "rojo", "azul", "gris"):
            self.color=color
        self.precioBase = precioBase
        self.comprobarConsumoEnergetico(consumo)
        self.peso = peso

    def comprobarConsumoEnergetico(self, letra):
        if letra in ("A","B","C","D","E","F"):
            self.consumo=letra
        else:
            self.consumo="A"

    def precioFinal(self):
        if self.consumo == 'A':
            self.precioBase = self.precioBase + 100
        elif self.consumo == 'B':
            self.precioBase = self.precioBase + 80
        elif self.consumo == 'C':
            self.precioBase = self.precioBase + 60
        elif self.consumo == 'D':
            self.precioBase = self.precioBase + 50
        elif self.consumo == 'E':
            self.precioBase = self.precioBase + 30
        elif self.consumo == 'F':
            self.precioBase = self.precioBase + 10

        if 0 < self.peso < 20:
            self.precioBase = self.precioBase + 10
        elif 20 < self.peso < 49:
            self.precioBase = self.precioBase + 50
        elif 50 < self.peso < 79:
            self.precioBase = self.precioBase + 80
        elif self.peso < 80:
            self.precioBase = self.precioBase + 100