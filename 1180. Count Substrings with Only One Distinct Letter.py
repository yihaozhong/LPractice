class Solution:
    def countLetters(self, s: str) -> int:
        count, total = 1, 1

        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count = 1
            else:
                count += 1
            total += count

        return total
