class Student:
    def __init__ (self, name, surname, age, speciality):
        self.name = name
        self.surname = surname
        self.age = age
        self.speciality = speciality

    def info(self):
        print('{} - {}, {} лет, {}'.format(self.name, self.surname, self.age, self.speciality))