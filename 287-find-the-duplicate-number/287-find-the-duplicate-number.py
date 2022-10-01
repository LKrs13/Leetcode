class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
         since each integer is between [1, len(nums)], we can think of the list 
         as a linked list because each number n will point at a nums[n] that is inside nums 
         (n being an index inside the list range [1, len(nums)])

         duplicated number will create a cycle 
         ex. [1,3,4,2,2], cycle at 2 
         1 -> 3 -> 2 -> 4
                   ^    |
                   |    |
                   |----|

        after using slow and fast pointers to detect the cycle, we can create
        another pointer at the beginning of the linked list. when moving this new pointer
        and the slow pointer by one, we are guaranteed that they will meet at the beginning of
        the cycle (aka the duplicated number).

        explanation:
        let c = distance of the cycle
            x = distance from intersection(slow, fast) and beginning of cycle
            p = distance from start of list and beginning of cycle

        2 * slow = fast
        2 (p + c - x) = p + c - x + c (fast goes through the cycle twice)
        p = x

        meaning that the new pointer (at position p) will be at the same distance from the
        slow pointer (at position x)
        '''
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            # moves the fast pointer twice
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow