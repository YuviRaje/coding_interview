'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        for i,each_interval in enumerate(intervals):
            if each_interval.start > new_interval.start:
                return intervals[:i-1] + self.merge_three_intervals(intervals[i-1], new_interval, each_interval) + intervals[i+1:]

            return intervals[:-1] + [self.merge_two_interval(intervals[-1], new_interval)]

        if intervals[-1].end > new_interval.start:
            return [self.merge_two_interval(intervals[-1], new_interval)]
        return intervals + [new_interval]


    def merge_three_intervals(self, first_interval, second_interval, third_interval):
        if first_interval.end > second_interval.start:
            merged_interval = self.merge_two_interval(first_interval, second_interval)

            if merged_interval.end > third_interval.start:
                merged_interval = self.merge_two_interval(merged_interval, third_interval)
                return [merged_interval]

            return [merged_interval, third_interval]

        elif second_interval.end > third_interval.start:
            merged_interval = self.merge_two_interval(second_interval, third_interval)

            return [first_interval, merged_interval]

        else:
            return [first_interval, second_interval, third_interval]

    def merge_two_interval(self, first_interval, second_interval):

        new_interval = Interval()
        new_interval.start = first_interval.start
        new_interval.end = max(first_interval.end, second_interval.end)

        return new_interval











