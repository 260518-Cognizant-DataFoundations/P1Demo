# The REPOSITORY LAYER is responsible for DB interactions
# CRUD Operations - Create Read Update Delete

from app.models.animal import Animal
import app.utils.db_connection_util as conn


# Get all animals from DB
def get_all_animals():
    connection = conn.get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM animals")
    results = cursor.fetchall()

    animals = []
    for row in results:
        animal = Animal(row[1], row[2], row[3], row[4], row[5])
        animals.append(animal)

    cursor.close()
    connection.close()

    return animals






# OLD STUFF below. It all still works, but we have graduated from fake databases.
# They're for babiessss


# First off, a fake database - just a Python Dictionary
# animals = {
#     1: Animal("Fluffy", "Lion", 200, 1.5, 4.5),
#     2: Animal("PanelData", "Panda", 100, 1.0, 4.8),
#     3: Animal("Antonio", "Tiger", 150, 1.2, 4.7),
#     4: Animal("Spear", "Wolf", 80, 0.8, 4.2)
# }
#
# # GET ALL animals
# def get_all_animals():
#     return animals.values()
#
# # GET animal by ID
# def get_animal_by_id(animal_id):
#     return animals.get(animal_id, None)
#
# # INSERT new animal
# def insert_animal(animal:Animal):
#     new_id = max(animals.keys()) + 1 # Get the highest ID and add 1 for the new ID
#     animals[new_id] = animal # Add the new animal with the ID as the key
#     return animals[new_id] # Return the created animal
#
# # UPDATE an animal by ID
# def update_animal(animal_id, updated_animal:Animal):
#
#     # TODO: Probably better to update fields instead of complete overwrites
#     # TODO: But I'm just keeping it simple
#
#     if animal_id in animals:
#         animals[animal_id] = updated_animal
#         return animals[animal_id]
#     else:
#         return None
#
#
# # TODO: Delete animal by ID