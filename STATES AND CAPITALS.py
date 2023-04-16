
import json


indian_states_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "West Bengal": "Kolkata"
}


with open("indian_states_capitals.json", "w") as json_file:
    json.dump(indian_states_capitals, json_file)

print("Indian states and capitals written to indian_states_capitals.json")
print(type(indian_states_capitals))