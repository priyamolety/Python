title = input("enter the title")

correct_format = ""

for char in title:
	if char.isupper():
		correct_format += " "+char
	else:
		correct_format+=char

print(correct_format.strip())
