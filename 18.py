class ListNode(object): #Remove Nth Node from End of List 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        sentinel = ListNode(0)
        sentinel.next = head
        
        length = 0
        current = head
        
        # Calculate length
        while current:
            length += 1
            current = current.next
        
        # Find node before the one to remove
        prev = sentinel
        for _ in range(length - n):
            prev = prev.next
        
        # Remove the nth node from end
        prev.next = prev.next.next
        
        return sentinel.next


# Helper function to print list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


# Example usage:
# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2

solution = Solution()
new_head = solution.removeNthFromEnd(head, n)

print_list(new_head)