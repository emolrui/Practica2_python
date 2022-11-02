import random


class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = "12345678X"
        self.sexo = 'M'
        self.peso = 0
        self.altura = 0

    def __init__(self, nombre="", edad=0, dni="", sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.generaDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return str(self.nombre) + "," + str(self.edad) + "," + str(self.dni) + "," + str(self.sexo) + "," + str(self.peso) + "," + str(self.altura)

    def calcularIMC(self):
        mci = self.peso / (self.altura ** 2)
        if mci<0:
            print(-1)
        elif mci==0:
            print(0)
        else:
            print(1)


    def esMayorDeEdad(self):
        return True if self.edad>=18 else False

    def introducirSexo(self, sexo):
        if sexo!='M' or sexo!='H':
            self.sexo = 'M'
        else:
            self.sexo = sexo

    def generaDNI(self):
        numero = random.randrange(10000000,99999999)

        dniChars = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        letra = dniChars[numero%23]
        self.dni = repr(numero) + letra