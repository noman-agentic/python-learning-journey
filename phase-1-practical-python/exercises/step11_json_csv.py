import json
import csv

profile = {
    "name": "Noman",
    "age": 40,
    "current_job": "Commercial Supervisor",
    "target_job": "AI Automation Engineer",
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["target_job"])

friends = [
    {"name": "Noman", "age": 40, "sex": "male"},
    {"name": "Tusher", "age": 39, "sex": "male"},
    {"name": "Rozina", "age": 39, "sex": "female"},
]

with open("friends.json", "w") as file:
    json.dump(friends, file, indent=4)


with open("friends.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "sex"])
    writer.writeheader()
    writer.writerows(friends)

with open("friends.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])