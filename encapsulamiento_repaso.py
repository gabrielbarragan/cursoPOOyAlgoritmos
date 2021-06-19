class CarrosEnVenta:
    def __init__(self, ciudad, marca, modelo, agencia, comprar):
        self.__ciudad = ciudad
        self.__marca = marca
        self.__modelo = modelo
        self.__agencia = agencia
        self.__disponibilidad = 'no disponible'
        self.__comprar = comprar

    @property
    def ciudad(self):
        return self.__ciudad
    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    @property
    def agencia(self):
        return self.__agencia
    @property
    def disponibilidad(self):
        return self.__disponibilidad
    @property
    def comprar(self):
        return self.__comprar
    @disponibilidad.setter
    def disponibilidad(self,disponibilidad):
        self.__disponibilidad = disponibilidad
    @ciudad.setter
    def ciudad(self,ciudad):
        if self.__disponibilidad == 'disponible':
            self.__ciudad = ciudad
        else:
            ValueError('El vehículo no se encuentra disponible')
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo
    @agencia.setter
    def agencia(self,agencia):
        if self.__disponibilidad == 'disponible':
            self.__agencia = agencia
        else:
            ValueError(f'El vehículo no se encuentra disponible')
    @comprar.setter
    def comprar(self, comprar):
        if self.__disponibilidad == 'disponible':
            self.__comprar = comprar
        else:
            ValueError(f'El vehículo no se encuentra disponible')

mi_vehiculo = CarrosEnVenta('Bucaramanga', 'Renault', '2010', 'Sanautos', 'Si')

print('_______ Antes de cambios __________')
print(mi_vehiculo.ciudad)
print(mi_vehiculo.marca)
print(mi_vehiculo.modelo)
print(mi_vehiculo.agencia)
print(mi_vehiculo.comprar)
print('_______ Despues de la venta __________')
mi_vehiculo.disponibilidad= 'disponible'
mi_vehiculo.ciudad = 'Bogotá'
mi_vehiculo.comprar = 'no'
mi_vehiculo.agencia = 'Particular'
print(mi_vehiculo.ciudad)
print(mi_vehiculo.comprar)
print(mi_vehiculo.agencia)



