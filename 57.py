def isSubsequence(s, t): #Is subsequence
    i = j = 0

    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


# Example usage 
s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))