class Car:
    def __init__(self, modelo, marca, color):
        self.modelo= modelo
        self.marca=marca
        self.color=color
        self._estado='en_reposo'
        self._motor=Motor(4)
    def acelerar(self, tipo='Lento'):
        if tipo=='rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'
        
class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0

    def inyecta_gasolina(cantidad_gasolina):
        pass
class Tire:
    def __init__(self, radio, width, height):
        self.radio=radio
        self.width=width
        self.height=height
        self._material='Caucho'
        self._estado='inflada'
    