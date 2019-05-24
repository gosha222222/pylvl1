class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)



class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)


class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=True)
