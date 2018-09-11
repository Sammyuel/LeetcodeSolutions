class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")
        for value1, value2 in zip(version1, version2):
            version1.pop(0)
            version2.pop(0)
            if int(value1) > int(value2):
                return 1
            if int(value2) > int(value1):
                return -1
        version1 = "".join(version1) or 0 
        version2 = "".join(version2) or 0
        version1 = int(version1)
        version2 = int(version2)
        if version2 > version1:
            return -1
        elif version2 < version1:
            return 1
        return 0