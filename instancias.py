class Coordenada:
    def __init__(self, lat, lon):
        self.lat=lat
        self.lon=lon
    def distancia(self, otra_coordenada):
        lon_delta=(self.lon - otra_coordenada.lon)**2
        lat_delta=(self.lat - otra_coordenada.lat)**2
        return (lon_delta + lat_delta)**0.5

if __name__=='__main__':
    coordenada_1 = Coordenada(3,30)
    coordenada_2 = Coordenada(4,8)
    
    print(coordenada_1.distancia(coordenada_2))
    print(isinstance(coordenada_2,Coordenada))