import json

data = {
    "name": "Vivek",
    "class": "BTech",
    "subject": "Computer Science",
    "year": 2026
}

json_data = json.dumps(data)

with open("student.json", "w") as f:
    f.write(json_data)

with open("student.json", "r") as f:
    loaded = json.load(f)

print(loaded)