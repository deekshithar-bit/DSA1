#Reversing Linked List
#Definition for a singly-linked list node
class ListNode:  
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Helper function to print list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
printList(head)

# Reverse the list
sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed List:")
printList(reversed_head)