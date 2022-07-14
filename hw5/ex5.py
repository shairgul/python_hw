f = open('number.txt', 'w')
f.write("4,2,3,3,8,5,4")
f.close()
f = open('number.txt', 'r')
number = f.read()
print(number)
f.close()
sum = 0
numbers = number.split(',')
for i in numbers:
    sum += int(i)
print(sum)
