#Add Two Numbers Represented by Linked Lists
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

        return dummy.next

# Helper function to create linked list from list
def create_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

# Helper function to print linked list
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example input:
l1 = create_list([23, 65, 31])  
l2 = create_list([50, 16, 47])  

# Solve
sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Output
print_list(result)