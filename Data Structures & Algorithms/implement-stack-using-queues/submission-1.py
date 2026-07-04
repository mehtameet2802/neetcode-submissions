class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        if not self.queue:
            self.queue.append(x)
        else:
            ele = self.queue[-1]
            self.queue.pop()
            self.push(x)
            self.queue.append(ele)

    def pop(self) -> int:
        ele = self.queue[0]
        if len(self.queue)>1:
            self.queue = self.queue[1:]
        else:
            self.queue = []
        return ele

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()