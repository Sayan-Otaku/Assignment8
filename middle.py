def insert_sting_middle(s1, s2):
	l1=len(s1)
	l1//=2
	return (s1[:l1]+s2+s1[l1:])

s1=input("Enter a string: - ")
s2=input("Enter another string: - ")
print(insert_sting_middle(s1,s2))
