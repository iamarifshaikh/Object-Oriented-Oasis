class Animal:
    def __init__(self,name,species,diet,age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age
        
    def feed(self):
        print(f"{self.name} the {self.species} is being fed {self.diet}.")
        
    def move(self):
        print(f"{self.name} the {self.species} is moving.")
        
    def make_sound(self):
        print(f"{self.name} is making a sound.")

class Mammal(Animal):
    def __init__(self,name,species,diet,age,fur_colour):
        super().__init__(name,species,diet,age)
        self.fur_colour = fur_colour

class Reptile(Animal):
    def __init__(self, name, species, diet, age,is_venomous):
        super().__init__(name, species, diet, age)
        self.is_venomous = is_venomous

class Bird(Animal):
    def __init__(self, name, species, diet, age,wing_span):
        super().__init__(name, species, diet, age)
        self.wing_span = wing_span

    def move(self):
        print(f"{self.name} the {self.species} is flying.")
        
class Enclosure:
    def __init__(self,name:str,capacity:int):
        self.name = name
        self.capacity = capacity
        self.animals = []
        
    def addAnimals(self,animal):
        if len(self.animals) >= self.capacity:
            print(f"{self.name} is full!")
        else:
            self.animals.append(animal)
            print(f"{animal.name} has been added to {self.name}.")
            
    def removeAnimals(self,name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} has been removed from {self.name}.")
                return
            else:
                print(f"{name} is not in {self.name}.")
    
    def listAnimals(self):
        print(f"Animals in {self.name}")
        for animal in self.animals:
            print(f"- {animal.name}, {animal.species}, {animal.diet}, {animal.age}")
    
class Staff:
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.assigned_enclosure = None    
        
    def assign_closure(self,enclosure):
        self.assigned_enclosure = enclosure
        print(f"{self.name} assigned to {enclosure.name}")
        
class Zoo:
    def __init__(self,name):
        self.name = name
        self.staff = []
        self.enclosures = []
    
    def addEnclosure(self,enclosure):
        self.enclosures.append(enclosure)
        print(f"Added enclosure: {enclosure.name}")
    
    def listEnosures(self):
        print(f"Enclosures in {self.name}:")
        for enclosure in self.enclosures:
            print(f"- {enclosure.name}, capacity: {enclosure.capacity}")
    
    def assignStaff(self, staff, enclosure):
        pass
        if enclosure in self.enclosures:
            staff.assign_closure(enclosure)
            self.staff.append(staff)
            print(f"{staff.name} has been assigned to {enclosure.name}.")
        else:
            print(f"Enclosure {enclosure.name} does not exist in the zoo.")