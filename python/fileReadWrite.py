
def read_file(file_path):
    with open(file_path, 'r') as file: # read() method runs only when 'r' option exists.
        content = file.read() # close automatically
        return content
    
try:
    content = read_file('sample.txt')
    print(content)
except FileNotFoundError:
    print("File not found.")
    
    
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        writing = file.write(data)
        return writing

data = "Hello, Python File I/O!\nThis is a test."
write_to_file('output.txt', data)

def append_to_file(file_path, data):
    with open(file_path, 'a') as file: # 'a' is appending contents option
        appending = file.write(data)
        return appending
append_data = "\nAppending this line to the file."
append_to_file('output.txt', append_data)