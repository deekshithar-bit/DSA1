def wordBreak(s, wordDict): #word break 
    dp = {}

    def fn(remS):
        if remS == "":
            return True

        if remS in dp:
            return dp[remS]

        res = False

        for i in range(len(remS)):
            substr = remS[:i + 1]

            if substr in wordDict and fn(remS[i + 1:]):
                res = True
                break

        dp[remS] = res
        return res

    return fn(s)


# Example 1
s = "leetcode"
wordDict = ["leet", "code"]

print(wordBreak(s, wordDict))