d = {1:2, 3:4, 4:3, 2:1, 0:0}
list_d = list(d.items())
print(list_d)
list_d.sort()
print(list_d)
list_d.sort(reverse=True)

print(list_d)
#(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)