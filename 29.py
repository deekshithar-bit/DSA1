def reverseStr(s: str, k: int) -> str: #Reverse String II 
    s = list(s)
    for i in range(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k])
    return ''.join(s)

# Example input
s = "deekshitha"
k = 2

print(reverseStr(s, k))