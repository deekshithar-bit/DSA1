def mySqrt(x: int) -> int: #Square root of x 
    if x < 2:
        return x

    l, r = 2, x // 2

    while l <= r:
        m = (l + r) // 2

        if m * m == x:
            return m
        elif m * m > x:
            r = m - 1
        else:
            l = m + 1

    return r


# Example usage
num = 8
result = mySqrt(num)

print("Square root of", num, "is:", result)