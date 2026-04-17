import json

data = {
    "name": "Vivek",
    "class": "BTech",
    "subject": "Computer Science",
    "year": 2026
}

json_data = json.dumps(data)

parsed = json.loads(json_data)

with open("student.json", "w") as f:
    json.dump(parsed, f)

with open("student.json", "r") as f:
    loaded = json.load(f)

print(parsed)
print(loaded)