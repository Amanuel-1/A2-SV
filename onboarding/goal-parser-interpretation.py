class Solution:
    def interpret(self, command: str) -> str:
        parsed  = []

        for i in range(len(command)-1) :
            c = command[i]
            if c=="G":
                parsed.append(c)
            elif c=="(":
                if command[i+1]==")":
                    parsed.append("o")
                else:
                    parsed.append("al")
        
        if command[-1]=="G":
            parsed.append("G")
        

        return "".join(parsed)
        