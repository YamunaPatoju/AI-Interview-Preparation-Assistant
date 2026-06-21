import re

text = """
Name: Daksh
Email: daksh@gmail.com
Phone: 9876543210
Skills: Python, SQL
"""

email = re.findall(r'\S+@\S+', text)

phone = re.findall(r'\d{10}', text)

print(email)
print(phone)