n = int(input("Enter the length of your integer array: "))
numbers = [0] * n
print(numbers)
numbers[0] = 10
numbers[-1] = -5
if( n % 2 != 0):
    numbers[int(len(numbers)/2)] = 3
    print(numbers)
else:
    print(numbers)