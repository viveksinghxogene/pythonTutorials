import json

data = {
    "name": "Vivek",
    "class": "BTech",
    "subject": "Computer Science",
    "year": 2026
}

json_string = json.dumps(data)

parsed = json.loads(json_string)

with open("student.json", "w") as f:
    json.dump(parsed, f)