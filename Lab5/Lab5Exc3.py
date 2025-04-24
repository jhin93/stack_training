
def Lab5Exc3():
    while True:
        vowel_count = 0
        input_sentence = input("Enter a sentence: ")
        if input_sentence == "*":
            break
        for i in input_sentence:
            if i in "aeiouwyAEIOUWY":
                vowel_count += 1
        print("Vowel count:", vowel_count)

Lab5Exc3()