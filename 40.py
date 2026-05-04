def removeOuterParentheses(s: str) -> str: #remove outer parenthesis 
    stack = []
    ans = ""

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            if len(stack) > 1:
                ans += s[i]
        else:
            if len(stack) > 1:
                ans += s[i]
            stack.pop()
    return ans

# Test input
s = "(()())(())"
print(removeOuterParentheses(s)) 