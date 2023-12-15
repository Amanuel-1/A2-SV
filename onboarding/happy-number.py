class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        mp = defaultdict(int)

        while num not in mp:
            if num == 1:
                return True

            mp[num] += 1
            s = str(num)
            next_num = 0
            for c in s:
                next_num += int(c) ** 2

            num = next_num

        return False