# Base class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says: Woof! Woof!"

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

# Subclass
class Bosco(Dog):
    def __init__(self):
        super().__init__("Bosco")  # Always named Bosco

# Example usage
my_dog = Bosco()
print(my_dog.bark())
print(my_dog.eat())
print(my_dog.sleep())
