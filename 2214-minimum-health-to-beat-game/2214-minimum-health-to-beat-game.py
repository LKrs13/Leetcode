class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        s = sum(damage)
        mx = max(damage)
        
        return s - min(mx, armor) + 1