import re

# Read data from file
with open("email.txt", "r") as file:
    text = file.read()

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

# Write emails to output file
with open("output.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print(emails)