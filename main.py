class Dog:
    def __init__(self,name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"{self.name}'s Status - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

def menu(pet):
    while True:
        print("\nChoose an action:")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. Show Tricks")
        print("6. Check Status")
        print("7. Exit")

        choice = input("Enter a number: ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter a trick to teach: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid choice, try again!")
my_pet = Dog("Buddy")
menu(my_pet)
