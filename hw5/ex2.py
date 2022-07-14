f = open('text.txt')
lines = 0
words = 0
for line in f:
    lines += 1
    words += len(line.split())
print("lines: ", lines)
print("words: ", words)

