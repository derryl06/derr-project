import math
a = int(input("angka pertama: "))
b = int(input("angka kedua: "))
print()

a2= int(math.pow(a, 2))
b2= int(math.pow(b, 2))
print(a, "pangkat 2 =", b2,"\n",b,"pangkat 2 =", a2)
print()

c2 = a2 + b2
print("hasil akar pangkat dari", a2, "+", b2, "=", math.sqrt(c2))

