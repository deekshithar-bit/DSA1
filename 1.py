def sum(a, b): #Sum of two numbers 
    add = a + b
    print(add)
sum(5, 3)

def second_largest(arr): #Second largest number
    if len(arr) < 2:
        return "Array should have at least two numbers"
    first = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else "No second largest found"

print(second_largest([0, 3, 5, 2, 7, 9]))  

class Solution: # palindrome number 
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_copy = x
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        return rev == x_copy

sol = Solution()
print(sol.isPalindrome(242)) 