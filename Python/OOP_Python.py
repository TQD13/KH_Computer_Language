################################################################################################################
# Python Class
class Dog:  # Create a class
    species = "Kiki"  # Class attribute

    def __init__(  # __init__ method is the constructor, called when a new object is created. Initialize instance attribute
        self,  # self parameter is a reference to the current instance of the class. Access the attributes and methods of the object
        name,
        age,
    ):
        self.name = name  # Instance attribute
        self.age = age

    def display_name(self):
        print(f"Dog's Name: {self.name}")


################################################################################################################
# Python Objects
dog_1 = Dog("Buddy", 3)  # Create an object of the dog class

# --------------------------------------------------------------------------------------------------------------
# Access class and instance variable
print(dog_1.name, dog_1.age)  # Instance variable
print(dog_1.species)  # Class variable

# --------------------------------------------------------------------------------------------------------------
# Modify instance variable, calss variable
dog_1.name = "Max"  # Update instance variable
dog_1.species = "Chihuahua"  # Update class variable
print(dog_1.name, dog_1.species)


################################################################################################################
# Python Inheritance
# --------------------------------------------------------------------------------------------------------------
# Single Inheritance: A child class inherits from a single parent class
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")


lab = Labrador("Buddy", 3)
lab.display_name()


# --------------------------------------------------------------------------------------------------------------
# Multiple Inheritance: A child class inherits from more than one parent class
class Friendly:
    def greet(self):
        print("Friendly!")


class Golden(Dog, Friendly):
    def sound(self):
        print("Golden Barks")


golden = Golden("Golden", 3)
golden.display_name()
golden.greet()
golden.sound()


# --------------------------------------------------------------------------------------------------------------
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} Guides the way!")


guide_dog = GuideDog("Max", 4)
guide_dog.display_name()
guide_dog.guide()


# --------------------------------------------------------------------------------------------------------------
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class

# --------------------------------------------------------------------------------------------------------------
# Hybrid Inheritance: A combination of two or more types of inheritance


################################################################################################################
# Python Polymorphism
# --------------------------------------------------------------------------------------------------------------
# Run-time Polymorphism: This type is determined during the execution of the program. Occur when a subclass with specific implementation for aldready defined method. Method overriding
class Labrador(Dog):
    def sound(self):  # Method overriding
        print("Labrador Barks")


class Beagle(Dog):
    def sound(self):  # Overriding parent method
        print("Beagle Barks")


dogs = [Labrador("Cow", 6), Beagle("Rabit", 7)]
for dog in dogs:
    dog.sound()  # Calls the appropriate method based on the object type


# Complile-time Polymorphism: This type is determined during the complilation of the program. Allow method with the same name to behave with different parameters
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Support multiple ways to call add()


calc = Calculator()
print(calc.add(5, 10))  # 2 arguments
print(calc.add(3, 7, 10))  # 3 arguments


################################################################################################################
# Python Encapsulation
class Cat:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute: accessible from anywhere
        self._breed = (
            breed  # Protected attribute: accessible within the class and its subclass
        )
        self.__age = age  # Private attribute: accessible only within the class. Access requires getter and setter methods

    def get_info(self):  # Public method
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    def get_age(self):  # Getter for private method
        return self.__age

    def set_age(self, age):  # Setter for private method
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


cat = Cat("Kitty", "USA", 3)
print(cat.name)  # Accessing Public Member
print(cat._breed)  # Accessing Protected Member but discouraged outside the class
print(cat.get_age())  # Accessing Private Member using getter
cat.set_age(5)  # Modifying Private Member using setter
print(cat.get_age())

################################################################################################################
# Data Abstraction
from abc import ABC, abstractmethod


class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")


class Labrador_1(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woofs!")


class Beagle_1(Dog):  # Partial Abstraction
    def sound(self):
        print("Barks Bark!")


dogs_1 = [Labrador_1("Buddy"), Beagle_1("Charlie")]
for dog in dogs_1:
    dog.display_name()  # Calls Concrete Method
    dog.sound()  # Calls implemented abstract method

# --------------------------------------------------------------------------------------------------------------
