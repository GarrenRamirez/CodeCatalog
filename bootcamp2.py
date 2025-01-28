class Astronaut:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Spaceship:
    def __init__(self, name, fuel, cargo, crew):
        self.name = name
        self.fuel = fuel
        self.cargo = cargo


    def __str__(self):
        return f"The {self.name} has {self.fuel} kilograms of fuel and is carring {self.cargo}."

    def travel(self, distance):
        self.fuel -= distance*10
        print(f"The {self.name} travels {distance} kilometers with {self.fuel} kilograms of fuel remaining.")

person1 = Astronaut("Walter", "Botanist")
person2 = Astronaut("Missy", "Engineer")
enterprise = Spaceship("Enterprise", 100, 10)
voyager = Spaceship("Voyager", 1000, 100)
aurora = Spaceship("Aurora", 2000, ["Water", "Chicken Nuggets", "Radioactive Isotopes"])

print(aurora)
aurora.travel(100)
print(aurora)

