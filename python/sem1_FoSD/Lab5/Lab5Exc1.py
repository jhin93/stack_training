import math

def Lab5Exc1func1(radius):
    radius_float = float(radius)
    perimeter = 2 * math.pi * radius_float
    perimeter_result = round(perimeter, 3)
    
    return perimeter_result

def Lab5Exc1func2(radius):
    radius_float = float(radius)
    area = math.pi * radius_float ** 2
    area_result = round(area, 3)
    return area_result

def Lab5Exc1func3(radius):
    radius_float = float(radius)
    volume = 4/3 * math.pi * radius_float ** 3
    volume_result = round(volume, 3)
    return volume_result

def Lab5Exc1():
    radius = input("Enter the radius of the circle: ")
    result1 = Lab5Exc1func1(radius)
    print("1. Calculate the perimeter of the circle", result1)
    result2 = Lab5Exc1func2(radius)
    print("2. Calculate the area of the circle", result2)
    result3 = Lab5Exc1func3(radius)
    print("3. Calculate the volume of the circle", result3)

Lab5Exc1()