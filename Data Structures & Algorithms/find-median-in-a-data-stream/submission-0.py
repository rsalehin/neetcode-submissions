class MedianFinder:

    def __init__(self):
        # small is the left side, large is the right side
        # small is a max-heap, large is a min-heap
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # Python by default implements min-heap. So, 
        # to create max-heap, make the num negative, thus
        # we can use min-heap. 
        heapq.heappush(self.small, -1 * num)

        # Make sure the every values in large is greater than small. 
        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # the sizes of small and large can vary by maximum 1

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large)> len(self.small):
            return self.large[0]
        return (-1*self.small[0]+ self.large[0])/2
        
        