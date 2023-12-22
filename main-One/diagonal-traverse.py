class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mp  = defaultdict(list)


        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mp[i+j].append(mat[i][j])
        

        flag =1
        answer=[]
        for n in mp:
            if flag ==1:
                answer.extend(mp[n][::-1])
            else:
                answer.extend(mp[n])
            flag*= -1


        return answer