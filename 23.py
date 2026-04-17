class ListNode(object): #Rotate List 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        steps = length - k
        prev = None
        curr = head
        for _ in range(steps):
            prev = curr
            curr = curr.next

        prev.next = None
        tail.next = head
        return curr


# Helper function to create linked list from list
def create_list(arr):
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Example
arr = [21, 42, 63, 84, 35]
k = 2

head = create_list(arr)

sol = Solution()
new_head = sol.rotateRight(head, k)

print_list(new_head)