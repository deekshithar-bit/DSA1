# first bad version 
bad = 4

def isBadVersion(version):
    return version >= bad


def firstBadVersion(n):
    l, r = 1, n

    while l < r:
        m = l + (r - l) // 2

        if not isBadVersion(m):
            l = m + 1
        else:
            r = m

    return r


# Test
n = 5
print(firstBadVersion(n))