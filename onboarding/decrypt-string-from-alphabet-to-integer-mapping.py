class Solution:
    def freqAlphabets(self, s: str) -> str:

        result  = ""
        stack = []
        start = ord("a")

        for i in range(len(s)):
            if len(stack)>1 and s[i]=="#":
                popped  = stack.pop()
                stack[-1]+= popped
            else:
                stack.append(s[i])


        return "".join([chr(start+int(i)-1) for i in stack])
        
        