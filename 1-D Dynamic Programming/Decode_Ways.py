class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        decode_one, decode_two = 1, 0
        n = len(s)

        for i in range(1, n):
            current = 0

            if 1 <= int(s[i]) <= 9:
                current += decode_one
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i == 1:
                    current += 1
                else:
                    current += decode_two

            decode_one, decode_two = current, decode_one

        return decode_one