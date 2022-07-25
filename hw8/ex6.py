class Equipment:

    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.validate_count()

    def validate_count(self):
        try:
            int(self.count)
        except:
            print(f"Напишите число для количества: {self.name}")

    def get_info(self):
        map = {"Название": self.name, "Количество": self.count}
        print(map)


class Printer(Equipment):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    def __str__(self):
        return f'{self.name} {self.count} {self.color}'


class Scanner(Equipment):
    def __init__(self,name, price, type_of_sensor):
        super().__init__(name, price)
        self.type_of_sensor = type_of_sensor

    def __str__(self):
        return f'{self.name} {self.count} {self.type_of_sensor}'




printer = Printer("epson printer", 16000, "red")
scanner = Scanner("epson scanner", "6000jkkj", "CIS")
print(printer)
print(scanner)
printer.get_info()
scanner.get_info()