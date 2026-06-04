import repositories.animal_repository as repo
import pandas as pd

# NOTE: This will be WAY less convoluted once we're working with a real SQL database

# Turn the animal dict into a dict of lists, so we can make a DataFrame
data = {
    animal_id: {
        "Name": animal.name,
        "Species": animal.species,
        "Weight": animal.weight,
        "Height": animal.height,
        "Guest Rating": animal.guest_rating
    }
    for animal_id, animal in repo.animals.items()
}
# "If using all scalar values, you must pass an index"
df = pd.DataFrame.from_dict(data, orient="index")


# I think we need to dissolve each animal object into standalone records, not objects
# yup

print(df)

# Find the average Guest Rating for all animals
average_rating = df["Guest Rating"].mean() # thx numpy

# Plot the animal ratings with a mean line------------
