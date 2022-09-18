class Solution:        
    def reorderList(self, head):
        # [1,2,3,4,5] 
        # find midpoint to 'separate' list: [1,2,(3),4,5] => think of it as 2 lists: [1,2,3] & [4,5]
        # reverse second half: [4,5] => [5,4]
        # zip two lists: [1,2,3] & [5,4] => [1,5,2,4,3]
        # find middle
        
        if not head:
            return []
        
        #step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # to remove cycle
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp