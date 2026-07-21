def numDecodings(s): #Decode Ways
    dp = {}

    def fn(remS):
        if remS == "":
            return 1
        if remS in dp:
            return dp[remS]

        n = len(remS)
        oneDigit = remS[n - 1:]
        twoDigit = remS[n - 2:] if n >= 2 else ""

        ans = 0

        if oneDigit != "0":
            ans += fn(remS[:n - 1])

        if len(twoDigit) == 2 and "10" <= twoDigit <= "26":
            ans += fn(remS[:n - 2])

        dp[remS] = ans
        return ans

    return fn(s)

# Example
s = "226"
print(numDecodings(s))