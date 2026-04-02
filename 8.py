class Solution(object): #Reverse String
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
s = ["h","e","l","l","o"]
print("Original String:",s)
Solution().reverseString(s)             
print("Reversed String:",s) 

class Solution(object): #Best Time to Buy and Sell Stocks
      def maxProfit(self, prices):
          maxProfit = 0
          for i in range(len(prices)):
              for j in range(i + 1, len(prices)):
                  profit = prices[j] - prices[i]
                  if profit > maxProfit:
                      maxProfit = profit
          return maxProfit
prices = [7,1,4,6,8,5]
result = Solution().maxProfit(prices)
print("Max Profit:",result)