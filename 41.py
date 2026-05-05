def evalRPN(arr): #Evaluate Reverse Polish Notation
    stack = []
    ops = {
        "+": lambda a, b: b + a,
        "-": lambda a, b: b - a,
        "*": lambda a, b: b * a,
        "/": lambda a, b: int(b / a)
    }
    for token in arr:
        if token in ops:
            a = stack.pop()
            b = stack.pop()
            ans = ops[token](a, b)
            stack.append(ans)
        else:
            stack.append(int(token))
    return stack.pop()

# Example input
arr = ["2", "1", "+", "3", "*"]

# Output
print(evalRPN(arr))