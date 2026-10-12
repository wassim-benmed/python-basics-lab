class Dog():
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def sit(self):
        print(self.name + " is now sitting")
    def roll_over(self):
        print(self.name + " rolled over!")
    def shout(self):
        print('Dog shouts')

dog = Dog("Husky", 2)
print(dog.name)
print(dog.get_age())
dog.sit()
dog.roll_over()
try:
    print(dog.__age)
except AttributeError as e:
    print("AttributeError:", e)

class Husky(Dog):
    def shout(self):
        print('woo')

class Tibetan_Mastiff(Dog):
    def shout(self):
        print('barking')

mydog = Husky('Larry', '3')
print(mydog.name)
print(mydog.get_age())

def sound(dog):
    dog.shout()

sound(Husky('Larry', 3))
sound(Dog('Richard', 2))
sound(Tibetan_Mastiff('Sylvia', 4))