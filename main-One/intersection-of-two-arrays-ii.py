class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1,freq2  =  Counter(nums1),Counter(nums2)
        answer  = []

        for m in freq1:
            if m in freq2:
                answer.extend([m]*min(freq1[m],freq2[m]))



        return answer
        


        