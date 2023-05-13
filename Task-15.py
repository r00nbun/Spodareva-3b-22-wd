class Car:
    def __init__ (self, mark, model, year, price):
        self.mark = mark
        self.model = model
        self.year = year
        self.price = price

    def info(self):
        print('{} - {}, {} год, {}'.format(self.mark, self.model, self.year, self.price))
