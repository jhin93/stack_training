# create a list of values
numbers = [10, 20, 30, 40]

# test whether specific values exist
print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)



# create a string
word = "Unix"

# store another name referring to the same original string
alias = word

# concatenation does not modify the original string in place
# it creates a new string object and rebinds word
word = word + " Systems"

# word now refers to the new string
print("word =", word)

# alias still refers to the original string
print("alias =", alias)

# create strings
x = "Unix"
y = "Unix"

# value equality checks whether the contents are the same
print(x == y)

# identity asks whether they are the same object
print(x is y)


# define strings using single and double quotes
a = 'Unix'
b = "Python"

# print both values
print(a)
print(b)


# define values to insert into a template
name = "Georges"
topic = "Python"

# use placeholders replaced by format()
print("Hello {}, welcome to {}.".format(name, topic))

# define a floating-point value
pi = 3.14159265

# format to two decimal places
print("Pi to two decimal places: {:.2f}".format(pi))