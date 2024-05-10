class Transaccion:
    
    TIPO = {
        'venta':'Venta'
        'abastecimiento':'Abastecimiento'
        }
    def __init__(self, tipo, cantidad, fecha):
        self.__tipo = (self.TIPO['venta'], self.TIPO['abastecimiento'])[tipo]
        self.__cantidad = cantidad
        self.__fecha = fecha
        
    
    def getTipo(self):
        return self.__tipo
    
    def getCantidad(self):
        return self.__cantidad
    
    def getFecha(self):
        return self.__fecha
    
    