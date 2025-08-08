import math

x1 = input("x1 coordinate of point A : ")
y1 = input("y1 coordinate of point A : ")
x2 = input("x2 coordinate of point B : ")
y2 = input("y2 coordinate of point B : ")

num_x1 = int(x1)
num_y1 = int(y1)
num_x2 = int(x2)
num_y2 = int(y2)

distance = math.sqrt((num_x2 - num_x1)**2 + (num_y2 - num_y1)**2)

print(round(distance, 2))