class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A_points, B_points, d = [], [], collections.defaultdict(int)

        # Filter points having 1 for each matrix respectively.
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    A_points.append((r, c))

                if B[r][c]:
                    B_points.append((r, c))
 
        # For every point in filtered A, calculate the
        # linear transformation vector with all points of filtered B
        # count the number of the pairs that have the same transformation vector.
        # Freq of transformation vectors will give the num of pairs from the first
        # matrix that are going to overlap the second matrix after transforming them the same way
        for r, c in A_points:
            for i, j in B_points:
                d[(i - r, j - c)] += 1

        return max(d.values() or [0])