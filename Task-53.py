class HouseholdTodoList:
    def __init__(self):
        with open('task53.txt', 'r') as file:
            self.lines = file.read()
            file.close()

    def add(self, string):
        with open('task53.txt', 'a') as file:
            file.writelines(string + '\n')
            file.close()
        return

    def delete(self, index):
        with open('task53.txt', 'r') as file:
            lines = file.readlines()
            del lines[index]
            file.close()
        with open('task53.txt', 'w') as file:
            file.writelines(lines)
            file.close()
        return

    def result(self):
        return print(self.lines)
