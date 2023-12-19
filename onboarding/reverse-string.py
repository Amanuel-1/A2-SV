class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        n = len(s)

        for i in range(len(s)//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]


