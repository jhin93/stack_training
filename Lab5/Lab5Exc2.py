import random
import math
import numpy as np

def Lab5Exc2func1():
    random_array = []
    for i in range(20):
        random_array.append(random.randint(1, 100))
    return random_array

def Lab5Exc2func2(random_array):
    # mean = sum(random_array) / len(random_array)
    mean = np.mean(random_array)
    return mean

def Lab5Exc2func3(random_array, mean):
    # standard_deviation = math.sqrt(sum((x - mean) ** 2 for x in random_array) / len(random_array))
    standard_deviation = np.std(random_array)
    return standard_deviation

def Lab5Exc2():
    random_array = Lab5Exc2func1()
    mean = Lab5Exc2func2(random_array)
    standard_deviation = round(Lab5Exc2func3(random_array, mean), 2)
    print("Random Array:", random_array)
    print("Mean:", mean)
    print("Standard Deviation:", standard_deviation)

Lab5Exc2()