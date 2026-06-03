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

    #TODO: validation

    # Call the repository method for extracting the animal data
    results = repo.get_all_animals()

    return results



