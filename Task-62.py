class robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def movement(self, time):
        result = time * self.speed
        print(self.name, " - ", self.speed*int(input()))
        print(f'{self.name} пройдёт {result} за {time}, при скорости {self.speed}')

class craw_robot(robot):
    def __init__(self, name, speed, territory):
        robot.__init__(self, name, speed)
        self.territory = territory

class wheel_robot(robot):
    def __init__(self, name, speed, mark):
        robot.__init__(self, name, speed)
        self.mark = mark