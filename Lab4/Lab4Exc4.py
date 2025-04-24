
def LabExc4():
    num_list = []
    while True:
        input_num = int(input("Enter a number: "))
        if input_num == -1:
            break
        
        num_list.append(input_num)
        # find max and min value
        max_value = max(num_list)
        min_value = min(num_list)
        

    print("max_value : ", max_value, "min_value : ", min_value)

LabExc4()