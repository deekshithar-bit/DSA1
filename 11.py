class Solution: #Single number
    def singleNumber(self, nums):
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        for num in nums:
            if hash[num] == 1:
                return num
nums = [4,1,2,1,2]            
print(Solution().singleNumber(nums))


class Node: #Linked list 
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        pass

# Create and print manually for testing
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

current = node1
while current:
    print(current.val)
    current = current.next    
