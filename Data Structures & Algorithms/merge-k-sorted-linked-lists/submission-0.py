# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(head1, head2):
            temp = ListNode()
            dummy = temp

            while head1 and head2:
                if head1.val <= head2.val:
                    temp.next = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next
            
            if head1:
                temp.next = head1
            
            if head2:
                temp.next = head2
            
            return dummy.next
        
        if len(lists) < 2:
            return None
        
        a = lists[0]

        for i in range(1, len(lists)):
            b = lists[i]
            a = merge(a,b)
        
        return a


        


