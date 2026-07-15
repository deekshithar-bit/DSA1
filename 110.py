def rob(val): # House robber problem 
    n = len(val)

    if n == 0:
        return 0
    if n == 1:
        return val[0]

    p1 = p2 = 0

    for i in range(n):
        curr = max(val[i] + p2, p1)
        p2 = p1
        p1 = curr

    return p1


# Example
val = [2, 7, 9, 3, 1]
print(rob(val))