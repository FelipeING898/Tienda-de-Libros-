from Libro import Libro


class TiendaLibros:

    def __init__(self):
        self.__caja = 1000000
        self.__cataLogo = []
    
    def buscarLibrosPorisbn(self, isbn):
        buscado = None
        for libro in self.__cataLogo:
            if libro.getIsbn() == isbn:
                buscado = libro
                break
        return buscado
    
    def buscarLibrosPorLibro(self, titulo):
        buscado = None
        for libro in self.__cataLogo:
            if libro.getTitulo() == titulo:
                buscado = libro
                break
        return buscado
    
    def RegistrarLibros(self, titulo, isbn, precioVenta, precioCompra, cantidad, rutaImagen):
        buscar = self.buscarLibrosPorisbn(isbn)
        nuevo = None
        if buscar is None:
            nuevo = Libro(titulo, isbn, precioVenta, precioCompra, cantidad, rutaImagen)
            self.__cataLogo.append(nuevo)

            return nuevo
        
    def EliminarLibro(self, isbn):
        buscar = self.buscarLibrosPorisbn(isbn)
        eliminado = False
        if buscar:
            if buscar.getCantidadActual() == 0:
                self.__cataLogo.remove(buscar)
                eliminado = True
            
            return eliminado 

# Buscar el libro más costoso.
# Buscar el libro menos costoso.
# Buscar el libro más vendido.

    def buscarLibroMasCostoso(self):
        