class Rectangle:
    def __init__ (self, height, width):
        self.height = height
        self.width = width
    
    def square(self):
        print('Площадь прямоугольника равна: ', self.height * self.width)