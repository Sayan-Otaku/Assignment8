def findSum(str1): 
    temp = "" 
    Sum = 0
    for ch in str1: 
        if (ch.isdigit()): 
            temp += ch 
        else: 
            Sum += int(temp) 
            temp = "0"

    return Sum + int(temp) 
  

str1 = input("Enter an alphanumeric string: - ")
  
print(findSum(str1))