import re

text = """
Contact sahil@gmail.com
or sahil@yahoo.com
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print(emails)