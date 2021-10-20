from math import *
print("Введите x: ")
x = float(input())
if x <= pi:
    y = x+2*x*sin(3*x)
elif x > pi:
    y = cos(x) + 2
print(y)