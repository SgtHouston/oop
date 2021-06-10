# Define a dictionary that holds our pet's attributes.
from cuddlypet import CuddlyPet
from pet import Pet
from toy import Toy

pet_name = input('What is your pet called? ')
pet_type = int(input("""
1. Pet
2. Cuddly Pet
which pet would you like? """))

if pet_type == 1:
    pet = Pet(pet_name)
elif pet_type == 2:
    pet = CuddlyPet(pet_name)

while True:
    print(pet)
    # Prompt the user to interact with the pet
    choice = int(input("""
1. Feed Pet
2. Play with pet
3. Do Nothing
4. Give toy
: """))
    if choice == 1:
        # 1. Feed Pet
        pet.eat_food()
    elif choice == 2:
        # 2. Play with pet
        pet.get_love()
    elif choice == 4:
        pet.give_toy(Toy())

    # Each time the loop runs, the pet will need some attention!
    pet.be_alive()
    if not pet.is_alive():
        print(pet)
        print(f'RIP {pet.name}')
        break