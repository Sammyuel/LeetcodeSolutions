
class Solution(object):
    def compress(self, chars):
        readPtr = 0
        writePtr = 0
        count = 1
        while readPtr < len(chars):
            if readPtr < len(chars) - 1 and chars[readPtr] == chars[readPtr + 1]:
                count += 1
            elif count > 1:
                chars[writePtr] = chars[readPtr]
                for digit in str(count):
                    writePtr+=1
                    chars[writePtr] = digit
                writePtr += 1
                count = 1
            else:
                chars[writePtr] = chars[readPtr]
                writePtr += 1
            readPtr += 1
        return writePtr 