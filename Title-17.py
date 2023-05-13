class Book:
    def __init__ (self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

    def info(self):
        print('{}, {} ({}), {}'.format(self.name, self.author, self.year, self.genre))