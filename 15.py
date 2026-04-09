#Checking Palindrome Linked List
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


# Create linked list: 1 -> 2 -> 2 -> 1 (palindrome)
head = ListNode(1)
second = ListNode(2)
third = ListNode(2)
fourth = ListNode(1)

head.next = second
second.next = third
third.next = fourth

# Test
sol = Solution()
print(sol.isPalindrome(head)) 


class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

# non-palindrome case: 1-> 2-> 3
# 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(sol.isPalindrome(head))