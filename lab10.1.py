import os
probel = 1
file = open("E:\\for10lab.txt", "r")
line = file.readline()
lenn = len(line)
for x in range(int(lenn)):
    if line[x] == " ":
        probel += 1
print("Предложение -", line)
print("Количество слов =", probel)
file.close()
