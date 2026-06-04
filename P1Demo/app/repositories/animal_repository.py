# The REPOSITORY LAYER is responsible for DB interactions
# CRUD Operations - Create Read Update Delete

from app.models.animal import Animal

# First off, a fake database - just a Python Dictionary
animals = {
    1: Animal("Fluffy", "Lion", 200, 1.5, 4.5),
    2: Animal("PanelData", "Panda", 100, 1.0, 4.8),
    3: Animal("Antonio", "Tiger", 150, 1.2, 4.7),
    4: Animal("Spear", "Wolf", 80, 0.8, 4.2)
}

# GET ALL animals
def get_all_animals():
    return animals.values()

# GET animal by ID
def get_animal_by_id(animal_id):
    return animals.get(animal_id, None)

# INSERT new animal
def insert_animal(animal:Animal):
    new_id = max(animals.keys()) + 1 # Get the highest ID and add 1 for the new ID
    animals[new_id] = animal # Add the new animal with the ID as the key
    return animals[new_id] # Return the created animal