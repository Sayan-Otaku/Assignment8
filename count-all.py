def Count(str): 
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)): 
        if str[i].isupper(): 
            upper += 1
        elif str[i].islower(): 
            lower += 1
        elif str[i].isdigit(): 
            number += 1
        else: 
            special += 1
    print('Upper case letters:', upper) 
    print('Lower case letters:', lower) 
    print('Number:', number) 
    print('Special characters:', special) 
  
str = input("Enter a complex text with uppercase, lowercase characters with digits and symbols")
Count(str) 