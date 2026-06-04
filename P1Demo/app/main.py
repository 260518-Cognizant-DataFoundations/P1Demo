import app.services.animal_services as service
from app.models.animal import Animal

# TODO: CLI!!

print(service.get_all_animals())

print(service.get_animal_by_id(3))
print(service.get_animal_by_id(10))

try:
    print(service.get_animal_by_id(-5))
except ValueError as e:
    print(e)

# print(service.insert_animal("Not an animal"))

print(service.insert_animal(Animal("Bubbles", "Dolphin", 150, 2.5, 4.9)))

print(service.update_animal(2, Animal("PanelData", "Panda", 110, 1.1, 4.9)))