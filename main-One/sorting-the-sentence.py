class Solution:
    def sortSentence(self, s: str) -> str:
        s  =  s.split()
        # zipp = zip((,)
        # anwer = ""


        s = sorted(s, key=lambda x:x[-1])

        print(s)


        return " ".join([e[:-1] for e in s])
        