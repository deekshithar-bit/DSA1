class ListNode(object): ##Intersection of two Linked Lists 
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        visited = set()
        
        # Traverse list B and store nodes
        while headB:
            visited.add(headB)
            headB = headB.next
        
        # Traverse list A and check intersection
        while headA:
            if headA in visited:
                return headA
            headA = headA.next
        
        return None
common = ListNode(8)
common.next = ListNode(10)

# List A: 3 -> 7 -> 8 -> 10
headA = ListNode(3)
headA.next = ListNode(7)
headA.next.next = common

# List B: 99 -> 1 -> 8 -> 10
headB = ListNode(99)
headB.next = ListNode(1)
headB.next.next = common

sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)

if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")