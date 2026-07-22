# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groups = 0
        prev = None

        total = 0
        temp = head

        while temp:
            total+=1
            temp = temp.next

        before = ListNode()
        dummy = before
        before.next = head
        cnt = 0

        while groups < total //k:

            while cnt<k:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
                cnt += 1
            
            new_before = before.next
            new_before.next = head
            before.next = prev
            before = new_before
            cnt = 0
            groups+=1


        return dummy.next


