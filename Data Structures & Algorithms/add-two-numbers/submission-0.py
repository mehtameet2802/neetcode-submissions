# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = 0
        carry = 0

        ans = ListNode()
        temp = ans

        while l1 or l2:
            if l1 and l2:
                sum = int(l1.val) + int(l2.val) + carry
                l1 = l1.next
                l2 = l2.next  
            elif l1:
                sum = int(l1.val) + carry
                l1 = l1.next 
            elif l2:
                sum = int(l2.val) + carry
                l2 = l2.next 
            
            carry = sum // 10
            value = sum % 10
            temp.next = ListNode(value)
            temp = temp.next
        
        if carry>0:
            temp.next = ListNode(carry)
        
        return ans.next
