import time

class Libro:
    books = []
    genre = "Libro"

    def __init__(self, name, autor, yearpublish, rating):
        self.name = name
        self.autor = autor
        self.yearpublish = yearpublish
        self.rating = rating
        self.books.append(self)

    def showbook(self):
        return f"Libro: {self.name} \n-Genero: {self.genre}\n-Autor: {self.autor}\n--Publicado: {self.yearpublish}\n---Rate: {self.rating}"

    def changename(self, namereplace):
        self.name = namereplace

    def changeautor(self, autorreplace):
        self.autor = autorreplace

    def changeyear(self, yearreplace):
        self.yearpublish = yearreplace

    def changerank(self, rate):
        self.rating = rate

    def getgenre(self):
        print(self.genre)

    def editBook(self):
        self.changename(input("Ingrese el nuevo nombre: "))
        self.changeautor(input("Ingrese el nuevo autor: "))
        self.changerank(input("Ingrese el nuevo año de publicacion: "))
        self.changerank(input("Ingrese la nueva puntuacion: "))
        print("Editado correctamente!")
        time.sleep(3)
    def deleteBook(self):
        for i in Libro.books:
            if i == self:
                Libro.books.remove(self)
