def isValid(s: str) -> bool: #Valid Parentheses    
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}

    for ch in s:
        if ch in pairs:
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if ch != pairs[top]:
                return False
    return len(stack) == 0


# Test cases
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))      # True