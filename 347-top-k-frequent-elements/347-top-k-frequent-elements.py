class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        res = []
        val = list(ct.values())
        heapq.heapify(val)
        
        kMost = heapq.nlargest(k, val)
        for i, j in ct.items():
            if j in kMost:
                res.append(i)
        
        return res