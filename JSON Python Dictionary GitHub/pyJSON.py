import json

# Sample data to write to the JSON file
data = {
    "name": "Nahum",
    "age": 35,
    "city": "Seattle",
    "is_employee": True,
    "skills": ["Python", "JavaScript", "SQL"]
}

# Writing JSON data to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been written to data.json")