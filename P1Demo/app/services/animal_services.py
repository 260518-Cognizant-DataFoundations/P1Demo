""" The SERVICE LAYER is for BUSINESS LOGIC

Business logic includes stuff like:
-User Input validation - did the user enter a valid value?
-Authentication - is the user logged in? Do they have permission?
-Data Manipulation - calculations, reformats, etc.

It serves as the bridge between what the user sees and the database
"""

# Import the repo layer so we can use their methods
import app.repositories.animal_repository as repo
from app.models.animal import Animal


# Get all animals
def get_all_animals():

    # Call the repository method for extracting the animal data
    results = repo.get_all_animals()

    # Not much to validate - but let's have a custom message for when there's no data
    if not results:
        return "No animals found! Go home!"

    return results


# Get animal by ID
def get_animal_by_id(animal_id):

    # Lots of stuff can validate for, now that there's user input
    # -is the input a number?
    # -is the input a valid number? (We'll do this one)
    # -does the input correspond to an actual record? (We'll do this one)

    # If the user passed in a number less than 1, it's not valid
    if animal_id < 1:
        raise ValueError("Animal ID must be 1 or higher!")

    # Call the repo method using the user's input
    result = repo.get_animal_by_id(animal_id)

    # If none, tell the user the animal ID they searched does not exist
    if not result:
        return f"Animal with ID {animal_id} not found! Try again!"

    return result


# Insert Animal
def insert_animal(animal):

    # Lots we could validate here as well
    # Realistically, we'd check every single animal field for validity

    # Ensure an animal object was passed in
    if not isinstance(animal, Animal):
        raise TypeError("Input does not seem to be an Animal object")

    # Check that species is not empty and not human
    if not animal.species or animal.species.lower() == "human":
        raise ValueError("Animal species cannot be empty or human!")

    # Ensure that weight and height are positive numbers
    if not isinstance(animal.weight, (int, float)) or not isinstance(animal.height, (int, float)):
        raise TypeError("Weight and Height must be numbers!")
    if animal.weight <= 0 or animal.height <= 0:
        raise ValueError("Weight an Height must be positive numbers!")

    # If validation checks pass, insert the new Animal!
    inserted_animal = repo.insert_animal(animal)

    # return a formatted message using the animal data
    return f"{inserted_animal.name} the {inserted_animal.species} has been added!"


# Update Animal
def update_animal(animal_id, updated_animal):

    # TODO: I'm not validating ANYTHING - we've seen examples of both above

    # Call the repo method to update the animal - NOTE, there are 2 possible outcomes from the repo

    result = repo.update_animal(animal_id, updated_animal)

    if not result:
        return f"Animal #{animal_id} not found! Try a different ID!"

    return f"Animal #{animal_id} updated: {result}"
