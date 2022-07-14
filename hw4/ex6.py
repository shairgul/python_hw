from itertools import count, cycle

print('Введите q для завершения')
for i in count(int(input("введите стартовое число: "))):
    print(i)
    quit = input()
    if quit=='q':
        break

for i in cycle((input("введите слова через пробел: ")).split()):
    print(i)
    quit = input()
    if quit=='q':
        break