class Solution(object):
    def generate(self, numRows):
        if not numRows:
            return []
        r = [[1]]
        for i in range(1, numRows):
            level = [1]
            previous = r[i-1]
            for j in range(len(previous) - 1):
                level.append(previous[j] + previous[j+1])
            level.append(1)
            r.append(level)
        return r