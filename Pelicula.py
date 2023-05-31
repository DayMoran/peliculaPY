#Cree una clase Libro que modele la informacion que se mantiene en una biblioteca 
#sobre cada libro: IdLibro (unico para cada libro), 
#titulo, autor, ISBN, paginas, edicion, editorial, lugar (ciudad y pais) 
#y si esta disponible. 
#La clase debe tener: propiedades, constructores. 
class Pelicula:
    def __init__(self, titulo, duracion, director, synopsis, anio, precio, disponible):
        self.Titulo = titulo
        self.Duracion = duracion
        self.Director = director
        self.Synopsis = synopsis
        self.Anio = anio
        self.Precio = precio
        self.Disponible = disponible
        
    '''def precio_mas_iva(self):
        if self.Precio:
            precio = float(self.Precio)
            return precio + (precio * Libro.iva)
        else:
            return 0.0'''


  