class MinStack: #Mini stack 
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val, val))
        else:
            minVal = min(val, self.s[-1][1])
            self.s.append((val, minVal))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Example usage
stack = MinStack()

stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)

print("Top:", stack.top())       # should be 2
print("Min:", stack.getMin())    # should be 2

stack.pop()

print("Top after pop:", stack.top())    # should be 7
print("Min after pop:", stack.getMin()) # should be 3