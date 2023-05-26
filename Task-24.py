class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def info(self):
        print('Сотрудник {}, {} лет, зарплата {}'.format(self.name, self.age, self.salary))

person = Employee('Геральт', 56, 600)
person.info()