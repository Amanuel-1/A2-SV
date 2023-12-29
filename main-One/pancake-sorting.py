class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer =[]
        for i in range(len(arr)):
            max  = (-float('inf'),-1)
            for j in range(len(arr)-i):
                if max[0]<arr[j]:
                    max  = (arr[j],j)

            j =max[1]
            
           

            first  = arr[:j+1][::-1]
            arr  = first+arr[j+1:]
            print(arr)

            arr  =arr[:len(arr)-i][::-1] + arr[len(arr)-i:]
            answer.append(j+1)
            answer.append(len(arr)-i)
            
            print(arr)
            print(max)
            print()
        print(arr)
        return answer
            
        