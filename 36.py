from collections import deque #stack using queues 

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        ans = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ans

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        front = self.q1.popleft()
        self.q2.append(front)
        self.q1, self.q2 = self.q2, self.q1
        return front

    def empty(self) -> bool:
        return len(self.q1) == 0


# ----------- Testing the stack -----------
stack = MyStack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.top())   # Should be 30
print("Popped:", stack.pop())       # Removes 30
print("Top element:", stack.top())  # Should be 20
print("Is empty:", stack.empty())   # False

stack.pop()
stack.pop()

print("Is empty:", stack.empty())   # True