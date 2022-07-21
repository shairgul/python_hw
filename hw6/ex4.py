class Car:

    def __init__(self, name, color, speed, is_police):
        self._name = name
        self._color = color
        self._speed = speed
        self._is_police = is_police

    def go(self):
        print(f"Машина {self._name} поехала")

    def stop(self):
        print(f"Машина {self._name} остановилась")

    def car_turn(self,side):
        print(f"Повернула {side}")

    def show_speed(self):
        print(str(self._speed))


class TownCar(Car):
    def _init_(self):
        super.__init__(self)


    def show_speed(self):
        if self._speed > 60:
            print(f"Превышение скорости")
        else:
            print(self._speed)


class SportCar(Car):
    def _init_(self):
        super.__init__(self)


class WorkCar(Car):
    def _init_(self):
        super. _init_(self)

    def show_speed(self):
        if self._speed > 40:
            print(f"Превышение скорости")
        else:
            print(self._speed)


class PoliceCar(Car):
    def _init_(self):
        super. __init__(self)


t = TownCar("Ford Fiesta", "Синий", 100, "Есть")
t.go()
t.stop()
t.car_turn("направо")
t.show_speed()
s = SportCar("Ferrari_Roma", "Серый",300, "Есть")
s.go()
s.stop()
s.car_turn("налево")
w = WorkCar("Daewoo Nexia", "Белый", 50 , "Есть")
w.go()
w.stop()
w.car_turn("направо")
w.show_speed()
p = PoliceCar("Toyota Prius","Белый",180 ,"Есть")
p.go()
p.stop()
p.car_turn("направо")