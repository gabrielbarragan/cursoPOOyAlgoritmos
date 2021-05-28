class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura

class Cuadrado(Rectangulo): #la clase cuadrado extiende a la clase rectangulo

    def __init__(self, lado):
        super().__init__(lado,lado)#funcion especial y permite obtener una referencia directa de la superclase (Rectangulo)
        #siempre que se inicialice una subclase se debe inicializar tambien la superclase

if __name__=='__main__':
    rectangulo= Rectangulo(3,4)
    print(rectangulo.area())
    cuadrado = Cuadrado(5)
    print(cuadrado.area())