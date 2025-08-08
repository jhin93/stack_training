import math


x = input('input value of x : ')
y = input('input value of y : ')

num_x = int(x)
num_y = int(y)

z = num_x ** num_y
print(z)
result = math.sqrt(z)
print(round(result, 2))