import random

# Step 1:
# Numbers has a numbers a field which is a list of integers
# Define a procedue "populate" that initializes the list as follows:
# List values are randomly generated integers between 1 and 100
# Read the initial list size from keyboard;
# Only populate the list if it is empty.
# Define a procedure "clear" that empties the list.
# Define a procedure "show" that shows the list

# Step 2:
# Define a function "number" that checks if a number exists in the list and returns the index of its first occurrence if so, otherwise returns -1
# Define a function "numbers" that returns the indices of all matches of a target
# Define a procedure "find" that reads a target value, and displays "target is at position" if found, otherwise displays "target does not exist"
# Define a procedure "findAll" that reads a target value, and displays the indices of all matches of a target, otherwise displays "target does not exist"
# Define a procedure "delete" that reads a target value, and deletes all matches of a target from the list
# Define a procedure "update" that reads a target value and a new value, and updates the first occurrence of the target with the new value, otherwise displays "target does not exist"

class Numbers:
    def __init__(self):
        self.list = []

    def populate(self):
        if len(self.list) == 0:
            self.list = [random.randint(1, 100) for _ in range(int(input("Enter the initial list size: ")))]

    def clear(self):
        if len(self.list) > 0:
            self.list.clear()

    def show(self):
        if len(self.list) > 0:
            print(self.list) 
            

numbers = Numbers()

def main():
    numbers.populate()
    numbers.show()
    numbers.clear()
    numbers.show()

if __name__ == "__main__":
    main()  
