class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name} moves in some way.")

class Dog(Animal):
    def move(self):
        print(f" {self.name} runs on four legs!")

class Fish(Animal):
    def move(self):
        print(f" {self.name} swims through water!")

class Bird(Animal):
    def move(self):
        print(f" {self.name} flies through the air!")

class Snake(Animal):
    def move(self):
        print(f" {self.name} slithers on the ground!")

# Let's create some animals
animals = [
    Dog("Buddy"),
    Fish("Nemo"),
    Bird("Tweety"),
    Snake("Mamba")
]

# Demonstrate polymorphism - same method name, different behaviors
print("=== How Animals Move ===")
for animal in animals:
    animal.move()
