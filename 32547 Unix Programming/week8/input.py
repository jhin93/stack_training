name = input("Who are you: ")

print(f"Hello {name}")

age = int(input("How old are you: "))
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")
