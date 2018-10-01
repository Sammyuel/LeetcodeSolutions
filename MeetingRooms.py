# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        start_times = []
        end_times = []
        for interval in intervals:
            start_times.append(interval.start)
            end_times.append(interval.end)
        start_times.sort()
        end_times.sort()
        print(start_times)
        print(end_times)
        for i in range(1, len(start_times)):
            if start_times[i] < end_times[i-1]:
                return False
        return True 
                
    