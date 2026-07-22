class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.head = ListNode()
        self.end = self.head
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        
        new_node = ListNode(value)
        self.end.next = new_node
        self.end = self.end.next
        
        self.size += 1

        if self.size == 1:
            self.head = self.end
        
        self.end.next = self.head
        return True
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        if self.size == 1:
            self.head = ListNode()
            self.end = self.head
        else:
            self.end.next = self.head.next
            self.head = self.head.next
        
        self.size -=1
        
        return True

        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.end.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()