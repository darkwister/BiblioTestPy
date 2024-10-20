from Class.Libro import Libro
# noinspection SpellCheckingInspection


class Novel(Libro):
    genre = "Novela"

    def __init__(self, name, autor, yearpublish, rating):
        super().__init__(name, autor, yearpublish, rating)
