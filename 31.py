def largestOddNumber(s: str) -> str: #Largest Odd Number in a String
    n = len(s) - 1
    while n >= 0:
        if int(s[n]) % 2 == 1:
            return s[:n+1]
        n -= 1
    return ""

print(largestOddNumber("52"))      
print(largestOddNumber("4206"))    
print(largestOddNumber("35427"))   
print(largestOddNumber("135790"))  