# 메인 파일 (Lab6Exc2.py)
from Lab6Exc1 import Person

class People:
    def __init__(self):
        self.first = Person.default_constructor()  # self 전달 제거
        self.second = Person('Tom', 33)

    def show(self):
        print(f"First: {self.first.name}, {self.first.age} | Second: {self.second.name}, {self.second.age}")

    def update(self):
        self.first.name = input("Enter your updated name: ")
        self.first.age = int(input("Enter your updated age: "))

def main():
    people = People()
    people.show()  
    people.update()  
    people.show()  

if __name__ == "__main__":
    main()