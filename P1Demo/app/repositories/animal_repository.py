# The REPOSITORY LAYER is responsible for DB interactions
# CRUD Operations - Create Read Update Delete

from app.models.animal import Animal
import app.utils.db_connection_util as conn


# GET all from DB
def get_all_animals():

    # Connect to DB, open a cursor, execute a SELECT
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM animals")

    results = cursor.fetchall() # Gets the results of the SELECT

    # Take each DB record, turn it into an Animal object, and append to a list
    animals = []
    for record in results:
        animal = Animal(record[1], record[2], record[3], record[4], record[5])
        animals.append(animal)

    # Clean up
    cursor.close()
    connection.close()

    # Return the animals!
    return animals

# GET ONE animal by ID
def get_animal_by_id(animal_id):

    # Same connection syntax
    connection = conn.get_connection()
    cursor = connection.cursor()

    # PARAMETERIZED SQL Query (it has a variable)
    cursor.execute("SELECT * FROM animals WHERE id = %s", (animal_id,))
    record = cursor.fetchone() # Only getting a single record

    # Clean up and return!
    cursor.close()
    connection.close()
    return Animal(record[1], record[2], record[3], record[4], record[5])

# Insert Animal in the DB
def insert_animal(animal:Animal):

    # Same connection/cursor syntax
    connection = conn.get_connection()
    cursor = connection.cursor()

    # Parameterized SQL Insert Statement
    cursor.execute("""
        INSERT INTO animals (name, species, weight, height, guest_rating)
        VALUES (%s, %s, %s, %s, %s)""",
        (animal.name, animal.species, animal.weight, animal.height, animal.guest_rating))

    # We made a change to the DB - we need to commit!
    connection.commit()

    # Returning the Animal we just inserted
    new_id = cursor.lastrowid # Get the ID of the last inserted record

    # Use the new ID to select the new Animal
    cursor.execute("SELECT * FROM animals WHERE id = %s", (new_id,))
    record = cursor.fetchone()

    # Clean up and Return the new Animal
    cursor.close()
    connection.close()
    return Animal(record[1], record[2], record[3], record[4], record[5])



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