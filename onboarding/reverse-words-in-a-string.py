class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        ans =""
        return " ".join(s[::-1])
        