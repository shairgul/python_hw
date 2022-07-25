class DivideBy0(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        try:
            print(self.a/self.b)
        except:
            print("на ноль делить нельзя")

divide = DivideBy0(100,0)
divide.divide()