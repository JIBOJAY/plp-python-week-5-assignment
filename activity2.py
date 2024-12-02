# Base class which is Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must define this method.")

# Derived class which is Bird
class Bird(Animal):
    def move(self):
        return f"{self.name} is flying in the sky. 🐦"

# Derived class which is Fish
class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming in the water. 🐟"

# Derived class which is Dog
class Dog(Animal):
    def move(self):
        return f"{self.name} is running on the ground. 🐕"

# Demonstrate polymorphism
bird = Bird("Sparrow")
fish = Fish("Goldfish")
dog = Dog("Labrador")

animals = [bird, fish, dog]

for animal in animals:
    print(animal.move())
