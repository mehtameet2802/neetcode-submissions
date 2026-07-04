class MyHashSet:

    def __init__(self):
        self.arr = [[] for _ in range(1000)]
        

    def add(self, key: int) -> None:
        i = key % 1000
        if key not in self.arr[i]:
            self.arr[i].append(key)

    def remove(self, key: int) -> None:
        i = key % 1000
        if key in self.arr[i]:
            self.arr[i].remove(key)

    def contains(self, key: int) -> bool:
        i = key % 1000
        if key in self.arr[i]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)