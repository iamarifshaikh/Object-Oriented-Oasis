# main.py
from zoo import Animal, Mammal, Bird, Reptile, Enclosure, Staff, Zoo

# Create a zoo
my_zoo = Zoo("My Awesome Zoo")

# Create enclosures
mammal_enclosure = Enclosure("Mammal Kingdom", 5)
bird_enclosure = Enclosure("Bird Paradise", 10)
reptile_enclosure = Enclosure("Reptile House", 3)

# Add enclosures to the zoo
my_zoo.addEnclosure(mammal_enclosure)
my_zoo.addEnclosure(bird_enclosure)
my_zoo.addEnclosure(reptile_enclosure)

# Create animals
lion = Mammal("Leo", "Lion", "Meat", 5, "Golden")
parrot = Bird("Polly", "Parrot", "Seeds", 2, 30)  # Wingspan in cm
python = Reptile("Slither", "Python", "Rodents", 4, False)

# Add animals to their respective enclosures
mammal_enclosure.addAnimals(lion)
bird_enclosure.addAnimals(parrot)
reptile_enclosure.addAnimals(python)

# List animals in each enclosure
mammal_enclosure.listAnimals()
bird_enclosure.listAnimals()
reptile_enclosure.listAnimals()

# Create staff
zookeeper_john = Staff("John", "Zookeeper")
vet_jane = Staff("Jane", "Veterinarian")

# Assign staff to enclosures
my_zoo.assignStaff(zookeeper_john, mammal_enclosure)
my_zoo.assignStaff(vet_jane, bird_enclosure)

# List enclosures in the zoo
my_zoo.listEnosures()

# Test animal behavior
lion.feed()
parrot.move()
python.make_sound()