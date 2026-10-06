"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        end_time = []

        for iv in intervals:
            if end_time and end_time[0] <= iv.start:
                heapq.heappop(end_time)
            heapq.heappush(end_time, iv.end)

        return len(end_time)
        