import os
import time

from Class.Biografia import Biografia
from Class.Comic import Comic
from Class.Libro import Libro
from Class.Novela import Novel

# noinspection SpellCheckingInspection

clear = lambda: os.system('cls')


def createBio(name, autor, year, rate):
    return Biografia(name, autor, year, rate)


def createNovel(name, autor, year, rate):
    return Novel(name, autor, year, rate)


def createComic(name, autor, year, rate):
    return Comic(name, autor, year, rate)


def booksFactory(kind):
    if kind == Comic:
        createComic(input("Ingrese el nombre: "),
                    input("Ingrese el autor del comic: "),
                    input("Ingrese el año de publicacion: "),
                    float(input("Calificacion: ")))
    if kind == Novel:
        createNovel(input("Ingrese el nombre: "),
                    input("Ingrese el autor de la novela: "),
                    input("Ingrese el año de publicacion: "),
                    float(input("Calificacion: ")))
    if kind == Biografia:
        createBio(input("Ingrese el nombre de la biografia: "),
                  input("Ingrese el autor: "),
                  input("Ingrese el año de publicacion: "),
                  float(input("Calificacion: ")))


def booksHandler():
    print("Que tipo desea?\n[1]Biografia [2]Comic [3]Novela")
    x = int(input("Eleccion:"))
    tipo = None
    if x == 1:
        tipo = Biografia
    elif x == 2:
        tipo = Comic
    elif x == 3:
        tipo = Novel
    booksFactory(tipo)
    clear()


def editBook():
    index = 1
    for x in Libro.books:
        print(f"{index}. \n{x.showbook()}")
        index += 1
    if(len(Libro.books) > 0):
        opc = int(input("\nCual deseas editar?\nEleccion:"))
        edit = Libro.books[(opc - 1)]
        edit.editBook()
    else:
        print("La lista esta vacia")


def deleteBook():
    index = 1
    for x in Libro.books:
        print(f"{index}. {x.showbook()}\n")
        index += 1
    if(len(Libro.books) > 0):
        opc = int(input("\nCual deseas eliminar?\nEleccion:"))
        delete = Libro.books[(opc - 1)]
        delete.deleteBook()
    else:
        print("La lista esta vacia")


def main():
    Libro.books = [
    createBio("Biografía de Steve Jobs", "Walter Isaacson", "2011", 4.5),
    createComic("Spider-Man", "Stan Lee", "1962", 4.8),
    createNovel("1984", "George Orwell", "1949", 4.7)
    ]

    run = True
    while run:
        clear()
        print("Bienvenido a la biblioteca\n1.Crear libro\n2.Editar libro\n3.Eliminar libro\n4.Visualizar\n5.Salir")
        opt = int(input("Opcion: "))
        if opt == 1:
            clear()
            booksHandler()
        elif opt == 2:
            clear()
            editBook()
        elif opt == 3:
            clear()
            deleteBook()
        elif opt == 4:
            clear()
            if(Libro.books.count == 0):
                print("La lista esta vacia!")
                break
            for x in Libro.books:
                book = x.showbook()
                print(book)
            input("Pulse enter para continuar...")
        elif opt == 5:
            print("SALIENDO DEL PROGRAMA!")
            run = False
        else:
            print("Esa opcion no esta presente! Pruebe otra")
            time.sleep(2)
            

if __name__ == "__main__":
    main()
