# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # modify l1 in place: go through l1 & l2 and add numbers together with prev rest,
        # replace l1 with unit of sum and keep rest for next calculation. 
        # if no number in l1 or l2: sum with rest if exists else return number
        
        m1, m2 = l1, l2
        while m1 and m2:
            m1 = m1.next
            m2 = m2.next
        head, node = l1, True
        if m2:
            node = False
            head = l2
            
        rest = 0
        while l1 or l2:
            if l1 and l2:
                s = l1.val + l2.val + rest
                if s >= 10:
                    s = s-10
                    rest = 1  
                else:
                    rest = 0
                if node:    
                    l1.val = s
                else:
                    l2.val = s
                l1 = l1.next
                l2 = l2.next
                
            elif l1 and not l2:
                s = l1.val + rest
                if s >= 10:
                    s = s-10
                    rest = 1
                else:
                    rest = 0
                l1.val = s
                l1 = l1.next
                
            else:
                s = l2.val + rest
                if s >= 10:
                    s = s-10
                    rest = 1
                else:
                    rest = 0
                l2.val = s
                l2 = l2.next
        
        cp = head
        if rest:
            while head.next:
                head = head.next
            head.next = ListNode(1)
        
        return cp