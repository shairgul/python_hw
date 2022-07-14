f = open('data1.txt', encoding="utf-8")
dict = {}
for i in f:
    i = i.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace("-", "").strip()
    a = i.split()
    subject = a[0]
    lessons = 0
    for j in range(1, len(a)):
        lessons += int(a[j])
    dict[subject] = str(lessons)
print(dict)
f.close()