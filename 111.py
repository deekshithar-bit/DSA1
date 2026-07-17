from typing import List #House Robber II 

def rob(val: List[int]) -> int:
    n = len(val)
    if n == 0:
        return 0
    if n == 1:
        return val[0]

    def rob_helper(start: int, end: int) -> int:
        p1 = 0
        p2 = 0
        for i in range(start, end + 1):
            curr = max(val[i] + p2, p1)
            temp = p1
            p1 = curr
            p2 = temp
        return p1

    return max(rob_helper(0, n - 2), rob_helper(1, n - 1))


# Example usage
val = [2, 3, 2]
print("Maximum money that can be robbed:", rob(val))