class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        int start = 0, end = 0, sum = 0, minLen = INT_MAX;
        while (end < n) {
            sum += nums[end++];
            while (sum >= s) {
                minLen = min(minLen, end - start);
                sum -= nums[start++];
            }
        }
        return minLen == INT_MAX ? 0 : minLen;
    }
};
