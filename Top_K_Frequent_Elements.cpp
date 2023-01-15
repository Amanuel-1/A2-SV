class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m ; 
        vector<pair<int,int>> mv ;
        vector<int> ans;
        for(int& i : nums){
            m[i]++;
        }

        
 for(auto& p : m){
     mv.push_back(p);
 }

 sort(mv.begin() , mv.end() , [](const auto& p1 ,const auto& p2){
     return p1.second > p2.second ;
 });

        for(int i = 0 ; i< k  ; i++){
            ans.emplace_back(mv[i].first);
        }
        return ans;
    }
};