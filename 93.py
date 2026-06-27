class Solution: #Palindrome Partitioning
    def partition(self, s: str): 
        result = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return

            for i in range(1, len(remaining) + 1):
                choice = remaining[:i]

                if not isPalindrome(choice):
                    continue

                path.append(choice)
                backtrack(path, remaining[i:])
                path.pop()

        backtrack([], s)
        return result


# Driver code
s = "aab"

solution = Solution()
output = solution.partition(s)

print(output)