import json

data = [
    {"RollNo": 45, "Name": "Sahil", "Marks": 90},
    {"RollNo": 68, "Name": "Sarthak", "Marks": 91},
    {"RollNo": 66, "Name": "Yug", "Marks": 92}
]

with open("info.json", "w") as file:
    json.dump(data, file)

print("Data Written Successfully!!")