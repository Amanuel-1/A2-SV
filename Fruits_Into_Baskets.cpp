class Solution {
public:
    int totalFruit(vector<int>& arr) {
        int n = arr.size();
        if(n == 1 || n == 2)
        {
            return n;
        }
        int k = 2; 
        
        int i = 0, j = 0;
        int mx = INT_MIN;
        unordered_map<int, int> mp;
        while(j < n)
        {
            mp[arr[j]]++;
            if(mp.size() < k)
            {
                j++;
            }
            else if(mp.size() == k) 
            {
                mx = max(mx, j - i + 1);
                j++;
            }
            else if(mp.size() > k) 
            {
               
                while(mp.size() > k)
                {
                    mp[arr[i]]--;
                    if(mp[arr[i]] == 0)
                    {
                        mp.erase(arr[i]);
                    }
                    i++; 
                }
                j++;
            }
        }
        if(mx == INT_MIN)
        {
            return n;
        }
        
        return mx; 
    }
};
