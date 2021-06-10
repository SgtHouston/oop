class Dog:
    # Class Attribute
    species = 'mammal'

    # Initialize / Instance Attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance Method
    def description(self):
        return f"A {self.breed} who is {self.age} year old named {self.name}"

    def bark_at(self, other_dog):
        print(f"{self.name} barked furiously at {other_dog.name}")


nelson = Dog('Nelson', 3, "Cavalier Spaniel")
baxter = Dog('Baxter', 16, "Basenji")

# print(nelson.description())
# print(baxter.description())

nelson.bark_at(baxter)