class Solution {
public:
     vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        vector<int> prefix_xor(n + 1);
        prefix_xor[0] = 0;
        for (int i = 1; i <= n; i++) {
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1];
        }
        vector<int> res;
        for (auto q : queries) {
            int l = q[0], r = q[1];
            res.push_back(prefix_xor[r + 1] ^ prefix_xor[l]);
        }
        
        return res;
     }
};
