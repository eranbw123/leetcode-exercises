
# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        winner = []
        current = []

        for char in s:
            if char in current:
                index = current.index(char)
                del current[:index + 1]
            current.append(char)
            if len(current) > len(winner):
                winner = current.copy()
        return len(winner)