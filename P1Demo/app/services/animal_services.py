""" The SERVICE LAYER is for BUSINESS LOGIC

Business logic includes stuff like:
-User Input validation - did the user enter a valid value?
-Authentication - is the user logged in? Do they have permission?
-Data Manipulation - calculations, reformats, etc.

It serves as the bridge between what the user sees and the database
"""

# Import the repo layer so we can use their methods
import app.repositories.animal_repository as repo

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
