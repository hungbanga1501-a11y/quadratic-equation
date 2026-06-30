import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b*b - 4*a*c

if a == 0:
    print("không hợp lệ")
elif d < 0:
    print("vô nghiệm")
elif d == 0:
    print("có nghiệm kép: x1 = 2x =", -b/(2*a))
else:
    print("Có 2 nghiệm: 1x =", (-b+math.sqrt(d))/(2*a),"2x =",(-b-math.sqrt(d))/(2*a))