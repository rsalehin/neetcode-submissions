class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use minHeap. As we will need the maximum two, we need to take the negative. 
        s = [-s for s in stones]
        heapq.heapify(s)
        while len(s)>1:
            first = -1* heapq.heappop(s)
            second = -1 * heapq.heappop(s)
            if first > second:
                heapq.heappush(s, -1*(first - second))
        heapq.heappush(s,0)
        return abs(s[0])