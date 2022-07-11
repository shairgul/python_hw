def fact(n):
    mult = 1
    for i in range(1, n + 1):
        mult *= i
        yield f'{i}! = {mult}'


for i in fact(int(input("Введите число: "))):
    print(i)
