import random

random.seed(10)

result = 0

def Lab4Exc6():

    global result
    input_num = int(input("input : "))
    numbers = [random.randint(1,100) for _ in range(input_num)]
    print(*numbers)
    result = sum(num for num in numbers if num % 2 == 0)
    print(result)

Lab4Exc6()