from sys import argv
try:
    time, rate, bonus = map(float, argv[1:])
    print(time*rate+bonus)
except Exception:
    print("Введите числа")
