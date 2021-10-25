import math
pi=3.14
a=pi/8
b=2/pi
step=(b-a)/15
while a<=b:
    print(math.sin(1/a))
    a+=step
