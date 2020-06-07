class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dis = []
        for p in points:
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            dis.append((d, p))
        heapq.heapify(dis)
        return [d[1] for d in heapq.nsmallest(K, dis)]