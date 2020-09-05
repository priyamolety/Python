k = input("enter your name")

refined =""

for char in k:
	if char.isalpha() or char == " ":
		refined += char
print(refined)
