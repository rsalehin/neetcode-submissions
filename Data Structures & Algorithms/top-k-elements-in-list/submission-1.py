class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        frequency_dict = {}

        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) +1 

        for num in frequency_dict.keys():
            heapq.heappush(heap, (frequency_dict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(k):
            most_frequent = heapq.heappop(heap)[1]
            result.append(most_frequent)
        return result
        