from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:

        self.stack.append(x)

        return

    def pop(self) -> int:

        dup = []

        for _ in range(len(self.stack)-1):

            dup.append(self.stack.popleft())

        pop = self.stack.popleft()

        self.stack = deque(dup)

        return pop


    def top(self) -> int:

        for i in range(len(self.stack)):
            if i == len(self.stack)-1:
                return self.stack[i]
        

    def empty(self) -> bool:

        if not self.stack:
            return True

        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()