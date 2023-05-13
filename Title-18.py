class Geometric_Figure:
    def __init__ (self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def info(self):
        print('Площадь - {}, периметр - {}'.format(self.square, self.perimeter))