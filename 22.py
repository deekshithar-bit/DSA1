class ListNode(object): #Merge two Sorted lists
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next

# Helper to create linked list
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper to print linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example input
list1 = create_list([18, 25, 43])
list2 = create_list([21, 36, 49])

# Run solution
sol = Solution()
result = sol.mergeTwoLists(list1, list2)

# Output
print_list(result)