class Student:
    def __init__ (self, name, surname, year, grades):
        self.name = name
        self.surname = surname
        self.year = year
        self.grades = grades
        
    def gpa(self):
        print('Средний балл равен: ', sum(self.grades)/len(self.grades))