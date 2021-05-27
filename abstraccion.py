class Lavadora:
    def __init__(self):
        pass
    
    def lavar(self, temperatura='ambiente',ciclo='normal',enjuague='No'):
        self.temperatura=temperatura
        self._llenar_tanque_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar(ciclo)
        self.enjuagar(enjuague)
        self._centrifugar()

    def _llenar_tanque_de_agua(self,temperatura):
        self.temperatura=temperatura
        print(f'Llenado del tanque con agua a temperatura {temperatura}')

    def _agregar_jabon(self):
        print('Agregando jabon...')

    def _lavar(self, ciclo):
        self.ciclo=ciclo
        print(f'Lavando en el ciclo {ciclo}')

    def enjuagar(self,enjuague):
        if enjuague=='Si':
            print(f'Aplicando el suavizante y enjuagando la ropa...')
        elif enjuague=='No':
            print(f'Enjuagando la ropa sin enjuague...')
        else:
            print(f'No se está enjuagando, revisar la lavadora')

    def _centrifugar(self):
        print('Centrifugando la ropa...')

if __name__=='__main__':
    lavadora = Lavadora()
    lavadora.lavar(enjuague='Si')
