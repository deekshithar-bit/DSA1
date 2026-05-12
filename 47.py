# Guess Number higher or lower
# Suppose the picked number is:
picked = 6

# Mock guess API
def guess(num):
    if num == picked:
        return 0
    elif num > picked:
        return -1
    else:
        return 1

def guessNumber(n):
    l, r = 1, n

    while l <= r:
        m = l + (r - l) // 2
        res = guess(m)

        if res == 0:
            return m
        elif res < 0:
            r = m - 1
        else:
            l = m + 1

    return -1


# Example
n = 10
print("Guessed Number:", guessNumber(n))

# How it works:
# If guess(m) returns -1, the picked number is lower than m, so search left half.
# If guess(m) returns 1, the picked number is higher than m, so search right half.
# If 0, the number is found.