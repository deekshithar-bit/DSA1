# Detect Linked List Cycle Using Hash Table
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


# --------- Example 1: Cycle exists ---------
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c
c.next = a   # creates a cycle

sol = Solution()
print(sol.hasCycle(a)) 

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# ---------Example 2: No cycle ---------
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c
c.next = None  # no cycle

print(sol.hasCycle(a))