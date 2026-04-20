class Solution(object): #Find words containing character
    def findWordsContaining(self, words, x):
        result = []
        for i, word in enumerate(words):
            for ch in word:
                if ch == x:
                    result.append(i)
                    break
        return result

# Example usage
sol = Solution()
words = ["apple", "banana", "cherry", "date"]
x = "a"

print(sol.findWordsContaining(words, x))