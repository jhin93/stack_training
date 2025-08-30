
name = input("Enter your name: ")
age = int(input("Enter your age: "))

is_adult = age >= 18
greeting = f"Hello, {name}! You are {'adult' if is_adult else 'not adult'}."
print(greeting)

user_info_dictionary = {"name :": name, "age :": age}
user_info_list = [name, age]
user_info_tuple = (name, age)

print("user_info_dictionary :", user_info_dictionary)
print("user_info_list : ", user_info_list)
print("user_info_tuple : ", user_info_tuple)
print("")
print("name의 타입:", type(name))
print("age의 타입:", type(age))
print("is_adult의 타입:", type(is_adult))
print("user_info의 타입:", type(user_info_dictionary))
print("user_list의 타입:", type(user_info_list))
print("user_tuple의 타입:", type(user_info_tuple))

# list vs tuple
# list는 수정 가능, tuple은 수정 불가능
# list는 [], tuple은 ()

tuple_in_dict = {(1, 2): "point"}  # 튜플은 딕셔너리 키로 사용 가능
# list_in_dict = {[1, 2]: "point"}  # 리스트는 키로 사용 불가: TypeError
user_info_list.append("seoul")
print("added user_info_list : ", user_info_list)
# user_info_tuple[0] = 10 # 에러 발생. 튜플은 수정 불가.

# Tuple은 수정할 수 없지만, += (추가하려는값 ,) 을 통해 기존 튜플에 새로운 값을 concatenate하여  새로운 튜플을 만들어낼 수 있다.
print("기존 튜플 :", user_info_tuple, "ID", id(user_info_tuple))
user_info_tuple += ("seoul",)
print("새로운 튜플 :", user_info_tuple, "ID", id(user_info_tuple))