from Class.Libro import Libro
# noinspection SpellCheckingInspection


class Comic(Libro):
    genre = "Comic"

    def __init__(self, name, autor, yearpublish, rating):
        super().__init__(name, autor, yearpublish, rating)
