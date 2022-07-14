f = open('data.txt', encoding="utf-8")
names = []
salaries = []
sum=0
for i in f:
    a = i.split()
    names.append(a[0])
    salaries.append(float(a[1]))
for i in range(0, len(salaries)):
    sum+=salaries[i]
    if salaries[i] < 20000:
        print(names[i])

print(sum/len(salaries))
