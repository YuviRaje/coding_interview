'''
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],
cl
return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        current_start = intervals[0].start
        current_end = intervals[0].end
        result = []

        for i in range(1, len(intervals)):
            if current_end >= intervals[i].start:
                current_end = max(current_end, intervals[i].end)
            else:

                result.append(Interval(current_start, current_end))

                current_start = intervals[i].start
                current_end = intervals[i].end

        result.append(Interval(current_start, current_end))

        return result


