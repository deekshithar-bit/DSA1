def findContentChildren(g, s): #Assign Cookies
    g.sort()
    s.sort()
    i = 0  
    j = 0  

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
            j += 1
        else:
            j += 1

    return i


# Example input
g = [1, 2, 3]   # children's greed factors
s = [1, 1]      # cookie sizes

result = findContentChildren(g, s)

print(result)