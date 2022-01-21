from typing import Text
text = "123nut"
number = [i for i in text if i.isdigit()]
number2 = int("".join(number))-1
print(number2)
print(text)