"""Q5: Create a JSON file and read data from it."""

import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "person.json")

data = {
    "name": "Gaurav",
    "age": 20,
    "skills": ["Python", "HTML", "CSS"],
    "address": {"city": "Delhi", "country": "India"},
}

# Create (write) the JSON file
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print("person.json created.")

# Read data back from it
with open(path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("\nData read from file:")
print("Name  :", loaded["name"])
print("Age   :", loaded["age"])
print("Skills:", ", ".join(loaded["skills"]))
print("City  :", loaded["address"]["city"])
