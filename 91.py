def letterCombinations(digits: str): #Letter Combinations of a Phone Number
    if not digits:
        return []

    letters = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = []

    def backtrack(path, index):
        if index == len(digits):
            result.append("".join(path))
            return

        for ch in letters[digits[index]]:
            path.append(ch)
            backtrack(path, index + 1)
            path.pop()

    backtrack([], 0)
    return result


class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    result.append(path.copy())
                return

            for i in range(start, 10):
                if total + i > n:
                    break

                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return result


sol = Solution()

print(letterCombinations("23"))
print(sol.combinationSum3(3, 7))