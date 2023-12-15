class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        checker = [1 if n % 2 == 0 else 0 for n in nums]
        answer = []
        sm = sum(n for n in nums if n % 2 == 0)

        for val, ind in queries:
            cur = nums[ind]
            nums[ind] += val

            if checker[ind] == 1:
                if nums[ind] % 2 != 0:
                    sm -= cur
                    checker[ind] = 0
                else:
                    sm += val
            else:
                if nums[ind] % 2 == 0:
                    sm += nums[ind]
                    checker[ind] = 1

            answer.append(sm)

        return answer