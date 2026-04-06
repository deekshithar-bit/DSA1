# Finding Middle of the Linked List
# Definition for a singly-linked list node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize two pointers at the head
        slow = head
        fast = head
        
        # Move fast two steps and slow one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When fast reaches the end, slow is at the middle
        return slow

# Helper function to create a linked list from a list and return the head
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

# Helper function to print linked list from a given node
def print_from_node(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# --- Example Usage ---
sol = Solution()

# Test Case 1: Odd length [1, 2, 3, 4, 5]
head1 = create_linked_list([1, 2, 3, 4, 5])
middle1 = sol.middleNode(head1)
print("Input: [1,2,3,4,5] -> Output middle node and onwards:", print_from_node(middle1))

# Test Case 2: Even length [1, 2, 3, 4, 5, 6]
head2 = create_linked_list([1, 2, 3, 4, 5, 6])
middle2 = sol.middleNode(head2)
print("Input: [1,2,3,4,5,6] -> Output middle node and onwards:", print_from_node(middle2))
