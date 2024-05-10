class Libro:

    def __init__(self, titulo, isbn, precioVenta, precioCompra, cantidad, rutaImagen):
        self.__titulo = titulo
        self.__isbn = isbn
        self.__PrecioVenta = precioVenta
        self.__precioCompra = precioCompra
        self.__cantidad = cantidad
        self.__rutaImagen = rutaImagen
        self.__transaccion = []


    def getTitulo(self):
        return self.__titulo
    
    def getIsbn(self):
        return self.__isbn 
    
    def getCantidad(self):
        return self.__cantidad
    
    def getPrecioVenta(self):
        return self.__PrecioVenta
    
    def getPrecioCompra(self):
        return self.__precioCompra
    
    def getRutaImagen(self):
        return self.__rutaImagen
    
