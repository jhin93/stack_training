class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def default_constructor(cls):  # cls로 클래스 자체를 받음
        return cls('John', 20)
    
    def getNameAge(self):
        return self.name, self.age
    
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
    

# person = Person("John", 20)
# print(person.getNameAge())
# person.setNameAge("Jane", 21)
# print(person.getNameAge())
    
    