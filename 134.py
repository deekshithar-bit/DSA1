class Solution(object): #Split a string in balanced strings
    def balancedStringSplit(self, s):
        temp = 0
        count = 0

        for ch in s:
            if ch == 'R':
                temp += 1
            else:
                temp -= 1

            if temp == 0:
                count += 1

        return count


# Example
s = "RLRRLLRLRL"
solution = Solution()
print(solution.balancedStringSplit(s))