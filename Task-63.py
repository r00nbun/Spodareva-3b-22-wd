class ProductCard:
    def __init__(self, name, price, amt):
        self.name = name
        self.price = price
        self.amt = amt


    def decrease(self, index):
        self.amt -= index
        if self.amt > 0:
            self.amt = self.amt
        else:
            self.amt = 'Ошибка. Товар закончился.'



    def change(self, plus, index):
        if plus == True:
            self.price += index
        else:
            self.price -= index
            if self.price > 0:
                self.price = self.price
            else:
                self.price = 'Ошибка.'


    def display(self):
        print(f'Название: {self.name}\nЦена: {self.price}\nКоличество: {self.amt}')


milk = ProductCard('milk', 120, 6)
milk.decrease(7)
milk.change(True, 300)
milk.display()
