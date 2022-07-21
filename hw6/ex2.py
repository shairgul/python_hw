class Road:
    def __init__(self, length, width ):
        self._length = length
        self._width = width

    def get_full_profit(self):
        print(f"{self._length} м * {self._width} м * 25 кг * 5 см = {int((self._length * self._width * 25 *5) / 1000)}")

r = Road(2000, 50)
r.get_full_profit()