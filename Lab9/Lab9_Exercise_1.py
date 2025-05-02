def vower_couting_file():
    fileHandler = open("Lab9/Lab9_Exercise_1.txt", "r")
    content = fileHandler.read()
    fileHandler.close()
    print(content)

def vower_writing_file():
    while True:
        fileHandler = open("Lab9/Lab9_Exercise_1.txt", "a")
        input_string = input("Enter a string: ")
        fileHandler.write(counting_vower(input_string))
        fileHandler.close()
        if input_string == "*":
            break

def counting_vower(input_string):
    # Make input_string lowercase
    input_string = input_string.lower()
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    w_count = 0
    y_count = 0
    for char in input_string:
        # switch case for each vowel
        match char:
            case "a":
                a_count += 1
            case "e":
                e_count += 1
            case "i":
                i_count += 1
            case "o":
                o_count += 1
            case "u":
                u_count += 1
            case "w":
                w_count += 1
            case "y":
                y_count += 1
    return "a ==> " + str(a_count) + "\n" + "e ==> " + str(e_count) + "\n" + "i ==> " + str(i_count) + "\n" + "o ==> " + str(o_count) + "\n" + "u ==> " + str(u_count) + "\n" + "w ==> " + str(w_count) + "\n" + "y ==> " + str(y_count) + "\n\n"
            

def main():
    vower_couting_file()
    vower_writing_file()

if __name__ == "__main__":
    main()
