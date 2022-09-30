class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
    Let l1 be the list we will return, and keep replacing values on l1. 
    [if not l1.next and l2: l1.next, l2.next = l2.next, l1.next] means that whenever 
    we reach the tail of l1, but did not reach the end of l2 yet, we will swap the links
    so that l1 becomes the longer list.
        '''
        carry, head = 0, l1
        while l1 or l2:
            if not l1.next and l2: l1.next, l2.next = l2.next, l1.next
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            carry, l1.val = divmod(val1 + val2 + carry, 10)
            
            prev = l1
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry: prev.next = ListNode(carry)
        return head