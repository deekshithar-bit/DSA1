class MyQueue: #queues using stack 
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Example usage
q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print(q.peek())   # front element
print(q.pop())    # removes front
print(q.empty())  # check if empty
print(q.pop())
print(q.pop())
print(q.empty())