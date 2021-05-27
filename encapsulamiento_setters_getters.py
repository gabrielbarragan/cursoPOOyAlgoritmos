class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    @property
    def region(self):
        return self.__region
    @property
    def identificador(self):
        return self.__identificador
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region=region
        else: 
            raise ValueError(f'La región {region} no es válida en {self.__pais}')
    @identificador.setter
    def identificador(self, identificador):
        if identificador == self.__identificador:
            self.__identificador=identificador
        else:
            raise ValueError(f'El identificador {identificador} no se puede asignar, el identificador debe ser {self.__identificador}')
class LugardeVacunacion:
    def __init__(self, ciudad, ips, direccion):
        self.__ciudad = ciudad
        self.__ips = ips
        self.__direccion = direccion
        self.__operacion = 'consultar'
    @property
    def ips(self):
        return self.__ips
    @property
    def direccion(self):
        return self.__direccion
    @property
    def operacion(self):
        return self.__operacion
    @property
    def ciudad(self):
        return self.__ciudad
    @operacion.setter
    def operacion(self,operacion):
        self.__operacion = operacion
    @ips.setter
    def ips(self,ips):
        if self.__operacion == 'Modificar':
            self.__ips = ips
        else:
            ValueError(f'La operación que está realizando es de Consultar')
    @direccion.setter
    def direccion(self,direccion):
        if self.__operacion == 'Modificar':
            self.__direccion = direccion
        else:
            ValueError(f'La operación que está realizando es de Consultar')
    @ciudad.setter
    def ciudad(self,ciudad):
        if self.__operacion == 'Modificar':
            self.__ciudad = ciudad
        else:
            ValueError(f'La operación que está realizando es de Consultar')

vacunacion = LugardeVacunacion('Bucaramanga','Clinica Chicamocha', 'Calle 6 #5-4')
print(vacunacion.ips)
print(vacunacion.ciudad)
print(vacunacion.direccion)
print(vacunacion.operacion)
print('_______ Despues de cambios __________')
vacunacion.operacion='Modificar'
vacunacion.ips='Foscal'
vacunacion.ciudad='Floridablanca' #Genera error pues no creamos el setter @ciudad.setter
vacunacion.direccion='calle 3 #2-1'
print(vacunacion.ips) #para poder imprimir cualquiera de estos debemos haber creado el @property de cada atributo
print(vacunacion.ciudad)
print(vacunacion.direccion)
print(vacunacion.operacion)





# casilla = CasillaDeVotacion(123, ['Ciudad de México', 'Morelos', 'Sinaloa'])
# print(casilla.region)
# casilla.region = 'Morelos'
# print(casilla.region)
# print('::::::::::::::::')
# print(casilla.identificador)
# casilla.identificador= 987
# print(casilla.identificador)

