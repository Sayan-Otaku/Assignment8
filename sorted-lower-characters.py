text=input("Enter a text: - ")
words = text.split()
lower = []
upper = []
for char in text:
	if char.islower():
		lower.append(char)
	else:
		upper.append(char)
sortedStr = ''.join(lower + upper)
print("\n final str with lowercase letters comes first:")
print(sortedStr)
