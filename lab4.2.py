x = str(input())
a = str(len(x))
for i in range(int(a)):
   if ord(x[i]) > 1039 and ord(x[i]) < 1072:
       print(x[i])
# print(ord('А')) # 1040
# print(ord('Я')) # 1071

