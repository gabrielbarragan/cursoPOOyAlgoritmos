class Robot:

    def __init__(self, velocidad, autonomia):
        self.velocidad = velocidad
        self.autonomia = autonomia

    def avanzar(self):
        distancia=self.velocidad/self.autonomia
        return f'moviendome {distancia} m'

    def girar(self, sentido):
        return f'Girando a {sentido}'

class miniRobot(Robot):
    def __init__(self, velocidad, autonomia):
        super().__init__(velocidad,autonomia)
    def avanzar(self):
        return f'{(self.velocidad/2)/(self.autonomia-0.5)} m'

if __name__=='__main__':
    motosaurio = Robot(30, 3)
    print(motosaurio.avanzar())
    print(motosaurio.girar('izquierda'))
    microracer = miniRobot(30, 3)
    print(microracer.avanzar())
    print(microracer.girar('izquierda'))