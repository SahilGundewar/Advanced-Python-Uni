import csv

with open("info.csv", "w") as file:

    writer = csv.writer(file)

    writer.writerow(["RollNo", "Name", "Marks"])

    writer.writerow([45, "Sahil", 90])

    writer.writerow([68, "Sarthak", 91])

    writer.writerow([66, "Yug", 92])

print("Data Written Successfully!!")