def Lab4Exc7():
    vowels = ['a', 'e', 'i', 'o', 'u', 'w', 'y']
    vowel_count = 0
    while True:
        user_input = input("Type a string and press enter: ")
        if user_input == ".":
            print("Exiting the program.")
            break
        
        for char in user_input.lower():
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
    print(f"Number of vowels: {vowel_count}")

Lab4Exc7()

                    