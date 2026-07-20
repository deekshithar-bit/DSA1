def longest_palindrome(s: str) -> str: #Longest Palindromic Substring
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start, end = 0, 0

    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, end = i, i + 1

    # Check for palindromes of length 3 or more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, end = i, j

    return s[start:end + 1]


# Example usage
s = "babad"
result = longest_palindrome(s)
print("Input:", s)
print("Longest Palindromic Substring:", result)