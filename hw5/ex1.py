f = open("data3.txt","w")
while True:
    string = input("Введите текст")
    if string=="":
        break
    f.write(f'{string}\n')
f.close()