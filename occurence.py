def count(s, c) : 
       
    res = 0
    for i in range(len(s)) : 
          
        if (s[i] == c): 
            res = res + 1
    return res 
      
      
# Driver code 
str= input("Enter a string: - ")
c = input("Enter a character to find its number of occurence: - ")
print(count(str, c)) 
