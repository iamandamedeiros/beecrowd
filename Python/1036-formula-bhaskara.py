import math
valores = input().split()
a, b, c = valores

a = float(a)
b = float(b)
c = float(c)

r1 = 0
r2 = 0

calc = (b*b)-(4*a*c)

if(calc <0 or a==0):
    print("Impossivel calcular")
else:
    calc = math.sqrt(calc)
    r1 = (-b+calc)/(2*a)
    r2 = (-b-calc)/(2*a)
    print("R1 = %.5f\nR2 = %.5f" %(r1,r2))