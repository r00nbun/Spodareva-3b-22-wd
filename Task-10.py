class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('Имя:', self.name, '\nВозраст:', self.age)