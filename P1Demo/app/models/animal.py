

class Animal:

    # constructor
    def __init__(self, name, species, weight, height, guest_rating):
        self.name = name
        self.species = species
        self.weight = weight
        self.height = height
        self.guest_rating = guest_rating

    # TODO: getters and setters (and private vars)

    # Here's the __str__ method which helps us print something readble when printing animals
    # (Instead of <app.models.animal.Animal object at 0x000001>)
    def __str__(self):
        return (f"Animal(Name: {self.name}, "
                f"Species: {self.species}, "
                f"Weight: {self.weight}kg, "
                f"Height: {self.height}m, "
                f"Guest Rating: {self.guest_rating}/5)")

    # We need this to print Animals from dictionaries
    def __repr__(self):
        return self.__str__()

    # TODO: def validate_animal() or something...
    # This would be a great way to encapsulate all the validation logic for animal objects
    # So we dont have to rewrite it every time!