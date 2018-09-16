class Solution(object):
    def exclusiveTime(self, n, logs):
        result = [0] * n 
        starts = []
        previous_time = 0 
        for i in range(len(logs)):
            info = logs[i].split(":")
            func = int(info[0])
            state = str(info[1])
            time = int(info[2])
            if state == "start":
                if starts:
                    result[starts[-1]] += time - previous_time
                starts.append(func)
                previous_time = time
            else:
                previous = starts.pop(-1)
                result[func] += time + 1 - previous_time 
                previous_time = time + 1
        return result
        