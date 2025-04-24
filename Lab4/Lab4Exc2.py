import random

result = []

def LabExc2(n):
    for i in range(1, n):
        result.append(random.randint(1,100))
    print(result)

LabExc2(20)



