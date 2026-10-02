import math as ms

a = 2
b = 13.13

temp = (((1 - ms.e ** a) / b) * ms.cos((b/a) * ms.pi) + ms.log(0.708) * b)
result = ms.cbrt(temp)

print(result)
