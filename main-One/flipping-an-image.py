class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(len(row)//2):
                if row[i]==row[len(row)-i-1]:
                    row[i],row[len(row)-i-1] = abs(1-row[i]),abs(1-row[i])
            if len(row)%2:
                row[len(row)//2] =abs(1-row[len(row)//2] )
        return image

                