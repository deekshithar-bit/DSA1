def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    x = 0
    while x < len(strs[0]):
        ch = strs[0][x]
        for i in range(1, len(strs)):
            if x == len(strs[i]) or strs[i][x] != ch:
                return strs[0][:x]
        x += 1
    return strs[0]

# Example input
strs = ["dishonest", "disaster", "disrespect"] 

# Function call
result = longestCommonPrefix(strs)

# Output
print(result) 
