import app.services.animal_services as service
from app.models.animal import Animal

# I took a graphic design class in high school
print("""
O============================||***||=============================O
  *~''~* Welcome to the Zoo Animal Management Application *~''~*
O============================||***||=============================O""")
print("\n(Let's assume you're logged in as a manager...)")

# The while menu will run until the user exits, which will turn this boolean false
show_menu = True

while show_menu:

    print("\nPlease enter your choice (1-5): ")
    print("-------------------------------")
    print("1. View all animals")
    print("2. View animal by ID")
    print("3. Insert new animal")
    print("4. Update existing animal")
    print("5. Exit")

    choice = input(">>> ")

    # choice 1 --------------------------------------------
    if choice == "1":
        results = service.get_all_animals()
        for animal in results:
            print(animal)

    # choice 2 --------------------------------------------
    elif choice == "2":
        try:
            animal_id = int(input("Enter the animal ID: "))
            print(service.get_animal_by_id(animal_id))
        except ValueError as e:
            print(e)

    # choice 3 --------------------------------------------
    elif choice == "3":
        name = input("Enter animal name: ")
        species = input("Enter animal species: ")
        weight = float(input("Enter animal weight (kg): "))
        height = float(input("Enter animal height (m): "))
        # PUTTING 0 FOR GUEST RATING! Let's just assume new animals aren't rated yet.
        new_animal = Animal(name, species, weight, height, 0)
        print(service.insert_animal(new_animal))

    # choice 4 (this one is kinda jank - no validation and needs all animal fields)----------
    elif choice == "4":
        try:
            animal_id = int(input("Enter the animal ID to update: "))
            name = input("Enter new animal name: ")
            species = input("Enter new animal species: ")
            weight = float(input("Enter new animal weight (kg): "))
            height = float(input("Enter new animal height (m): "))
            guest_rating = float(input("Enter new guest rating (0-5): "))
            updated_animal = Animal(name, species, weight, height, guest_rating)
            result = service.update_animal(animal_id, updated_animal)
            print(result)
        except ValueError as e:
            print(e)

    # choice 5 --------------------------------------------
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        show_menu = False












# Commented out all the direct calls to service----------
#
# print(service.get_all_animals())
#
# print(service.get_animal_by_id(3))
# print(service.get_animal_by_id(10))
#
# try:
#     print(service.get_animal_by_id(-5))
# except ValueError as e:
#     print(e)
#
# # print(service.insert_animal("Not an animal"))
#
# print(service.insert_animal(Animal("Bubbles", "Dolphin", 150, 2.5, 4.9)))
#
# print(service.update_animal(2, Animal("PanelData", "Panda", 110, 1.1, 4.9)))