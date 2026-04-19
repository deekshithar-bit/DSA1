class Solution(object): #Find the length of last word using two loops
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        count = 0
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count

# Example usage
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))       # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6