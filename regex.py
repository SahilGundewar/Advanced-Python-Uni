import re

text = "I Have 1650 TI Graphics Card."

numbers = re.findall(r"\d+", text)

print(numbers)


import re

text = "Tomorrow Is Holiday"

result = re.findall("[A-Z]", text)

print(result)



import re

text = "Contact me at 1234567890, 9191919191"

result = re.findall(r"\d{10}", text)

print(result)