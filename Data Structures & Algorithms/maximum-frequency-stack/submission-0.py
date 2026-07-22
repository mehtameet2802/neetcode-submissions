from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.c_map = defaultdict(int)
        self.f_map = defaultdict(list)
        self.max_f = 0
        

    def push(self, val: int) -> None:
        self.c_map[val] += 1
        new_f = self.c_map[val]
        self.max_f = max(self.max_f, new_f)
        self.f_map[self.c_map[val]].append(val)

    def pop(self) -> int:
        ele = self.f_map[self.max_f].pop()
        self.c_map[ele] -= 1

        if not self.f_map[self.max_f]:
            self.max_f -= 1

        return ele
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()