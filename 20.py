class ListNode(object): # Odd Even Linked List 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

# Helper function to create linked list from list
def create_list(arr):
    head = ListNode(arr[0])
    current = head
    for x in arr[1:]:
        current.next = ListNode(x)
        current = current.next
    return head

# Helper function to print linked list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example
arr = [11, 24, 35, 46, 59, 62, 73]
head = create_list(arr)

sol = Solution()
new_head = sol.oddEvenList(head)

print(print_list(new_head))