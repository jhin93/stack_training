import math

r = input("Enter circle radius : ")
num_r = int(r)
circle_area = math.pi*(num_r**2)
sphere_volume = (4/3)*math.pi*(num_r**3)

print("value of radius go here : ", round(circle_area, 2))
print("value of radius go here : ", round(sphere_volume, 2))