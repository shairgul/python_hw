class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def format_date(cls, date):
        a = date.split('-')
        print(f'год = {a[0]}\nмесяц = {a[1]}\nдень = {a[2]}')

    @staticmethod
    def validate_date(date):
        a = date.split("-")
        if 1 > int(a[2]) or int(a[2]) > 31:
            print("день должен быть в диапозоне 1-31")
        elif 1 > int(a[1]) or int(a[1]) > 12:
            print("месяц должен быть в диапозоне 1-12")
        elif int(a[0]) <= 0:
            print("год должен быть больше нуля")
        else:
            print("Дата верная")


Date.format_date("2022-71-9")
Date.validate_date("2022-71-9")
