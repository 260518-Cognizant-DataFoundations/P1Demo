import app.services.animal_services as service

# TODO: CLI!!

print(service.get_all_animals())

print(service.get_animal_by_id(3))
print(service.get_animal_by_id(10))

try:
    print(service.get_animal_by_id(-5))
except ValueError as e:
    print(e)