# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        startTimes = []
        endTimes = []
        result = 0
        rooms = 0
        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        startTimes.sort()
        endTimes.sort()
        meetingEnd = endTimes.pop(0)
        for start in startTimes:
            if start >= meetingEnd:
                meetingEnd = endTimes.pop(0)
            else:
                rooms += 1
            if rooms > result:
                result = rooms
        return result
            
                
            