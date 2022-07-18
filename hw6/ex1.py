import time

class TrafficLight:

    _color = "Черный"

    def running(self):
        while True:
            print("Красный")
            time.sleep(7)
            print("Желтый")
            time.sleep(2)
            print("Зеленый")
            time.sleep(5)
            print("Желтый")
            time.sleep(2)

t = TrafficLight()
t.running()



