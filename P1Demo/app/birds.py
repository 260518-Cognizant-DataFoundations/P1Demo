# You've stumbled upon the solution to the data science assignment I'm dropping on Friday
# Since it's optional, and we won't present, I'll just paste a basic solution here
# It may help as an example for the data science reqs in your project

import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON file into a DataFrame
# pandas can read JSON just like CSV!
df = pd.read_json("data/birds.json")

# Remove the record with "Blue Whale" as the species
df = df[df["species"] != "Blue Whale"]

# Overwrite the old birds.json with the cleaned data
df.to_json("data/birds.json", orient="records", indent=4)

# Group total sightings by time of day
sightings_by_time = df.groupby("time_of_day")["sightings"].sum()

# Sort chronologically instead of alphabetically. Just thought this was a cool idea
time_order = ["Morning", "Afternoon", "Evening"]
sightings_by_time = sightings_by_time.reindex(time_order) # reindex reorders the index! wow

# Copilot put this here and I said "ok cool". Assignment doesn't call for it.
print("\n===== Sightings by Time of Day =====")
print(sightings_by_time)

# Plotting it
plt.bar(sightings_by_time.index, sightings_by_time.values,
        color=["steelblue", "coral", "seagreen"])

plt.title("Summer Bird Sightings by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Total Sightings")
plt.grid(True, alpha=0.3, axis="y")
plt.show()