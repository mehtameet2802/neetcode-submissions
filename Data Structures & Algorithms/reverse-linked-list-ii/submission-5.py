# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        cnt = 0

        temp = dummy
        prev = None
        while cnt<left:
            prev = temp
            temp = temp.next
            cnt+=1
        
        before = prev
        end = start = temp

        prev = None
        while cnt<=right:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
            cnt+=1
        
        before.next = prev
        end.next = start
        
        return dummy.next



        


        
