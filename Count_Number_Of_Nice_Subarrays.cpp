class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefix_odd(n + 1);
        prefix_odd[0] = 0;
        for (int i = 1; i <= n; i++) {
            prefix_odd[i] = prefix_odd[i - 1] + (nums[i - 1] & 1);
        }
        int res = 0;
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        for (int i = 1; i <= n; i++) {
            res += cnt[prefix_odd[i] - k];
            cnt[prefix_odd[i]]++;
        }
        
        return res;
    }
};
