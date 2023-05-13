class Dog:
    def __init__ (self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def info(self):
        print('Имя:', self.name, '\nПорода: ', self.breed,'\nВозраст:', self.age)