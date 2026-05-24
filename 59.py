class ListNode: #Intersection of Two Linked Lists
    def __init__(self, val=0):
        self.val = val
        self.next = None


def getIntersectionNode(headA, headB):
    pA = headA
    pB = headB

    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    return pA


# Create intersecting linked lists
#
# List A: 4 -> 1 \
#                  8 -> 4 -> 5
# List B:      5 -> 6 -> 1 /

# Common part
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# List A
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

# List B
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

# Find intersection
intersection = getIntersectionNode(headA, headB)

# Output
if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")