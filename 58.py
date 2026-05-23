def strStr(haystack, needle): # Finding Index of First Occurrence in String
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        for j in range(m):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i

    return -1


# Example usage
haystack = "hello"
needle = "ll"

result = strStr(haystack, needle)
print(result)