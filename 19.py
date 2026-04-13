class ListNode(object): # Remove Duplicates from Sorted List
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

# Helper function to print linked list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Create example linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(31)
head.next = ListNode(31)
head.next.next = ListNode(29)
head.next.next.next = ListNode(36)
head.next.next.next.next = ListNode(23)

# Run solution
sol = Solution()
new_head = sol.deleteDuplicates(head)

# Output result
print_list(new_head)