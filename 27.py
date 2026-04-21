class Solution(object): #Jewels and Stones 
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for s in stones:
            for j in jewels:
                if s == j:
                    count += 1
                    break
        return count

# Example usage
jewels = "aA"
stones = "aAAAAbbbb"

sol = Solution()
output = sol.numJewelsInStones(jewels, stones)
print(output)