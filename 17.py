class ListNode(object): #Remove Linked list elements 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head
        current = sentinel
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return sentinel.next

# Helper function to create linked list from Python list
def create_list(arr):
    dummy = ListNode(0)
    current = dummy
    for x in arr:
        current.next = ListNode(x)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
head = create_list([1, 2, 6, 3, 4, 5, 6])
val = 6

solution = Solution()
new_head = solution.removeElements(head, val)

print_list(new_head)