from Class.Libro import Libro


class Biografia(Libro):
    genre = "Biografia"

    def __init__(self, name, autor, yearpublish, rating):
        super().__init__(name, autor, yearpublish, rating)
