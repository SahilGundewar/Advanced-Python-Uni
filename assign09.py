import csv
import json

data = []

with open("info.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)

with open("info.json", "w") as file:
    json.dump(data, file)

print("Converted Successfully!!")