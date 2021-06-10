from pet import Pet


class CuddlyPet(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.hunger += 2

    def cuddle(self, other_pet):
        other_pet.get_love()

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()