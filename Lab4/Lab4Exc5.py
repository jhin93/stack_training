
def LabExc5():
    while True:
        input_num = int(input("Enter a number: "))
        if input_num == -1:
            break
        even_sum = 0
        for i in range(0, input_num + 1):
                if i % 2 == 0:
                     even_sum += i
        print(even_sum)


LabExc5()