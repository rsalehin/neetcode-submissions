"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        start_pointer, end_pointer = 0, 0

        while start_pointer < len(start):
            if start[start_pointer] < end[end_pointer]:
                count += 1
                start_pointer += 1
            else:
                count -= 1
                end_pointer += 1
            res = max(res, count)
        return res
        