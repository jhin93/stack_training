
squares = [x**2 for x in range(1, 11)]
print(squares)

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)

names = ["kim", "lee", "park", "choi", "jung"]
long_names = [name.upper() for name in names if len(name) >= 4]
print(long_names)

triple_list = [x for x in range(1, 20) if x % 3 == 0]
print(triple_list)

words = ["apple", "bat", "cat", "dog", "elephant"]
word_lengths_under_4 = [word for word in words if len(word) <= 4]
print(word_lengths_under_4)