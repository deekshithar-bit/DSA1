def countSubstrings(s): #Palindromic Substrings
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = 0

    # Length 1 substrings
    for i in range(n):
        dp[i][i] = True
        ans += 1

    # Length 2 substrings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans += 1

    # Length >= 3 substrings
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                ans += 1

    return ans


# Example
s = "aaa"
print(countSubstrings(s))