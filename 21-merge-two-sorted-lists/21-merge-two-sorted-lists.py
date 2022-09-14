# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                # create node for head.next instead of head 
                # => able to move to it after
                head.next = ListNode(list1.val)
                list1 = list1.next
            
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next
            
            head = head.next
        
        # Si l'une des listes n'est pas vide et que l'autre est vide,
        # ajoutez la liste non vide 
        head.next = list1 or list2
        
        return dummy.next
                