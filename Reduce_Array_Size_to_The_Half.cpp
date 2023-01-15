class Solution {
public:
    int minSetSize(vector<int>& arr) {
       //unordered_map<int,int> m;
       int len  = arr.size() ,subtr=len,i = 0,c=0;
      // vector<int> mv ; 

        unordered_map<int,int> m ; 
        vector<int> mv ;
        vector<int> ans;
        for(int& i : arr){
            m[i]++;
        }

        
 for(const auto& p : m){
     mv.push_back(p.second);
 }


 sort(mv.rbegin(),mv.rend());

   for(int n : mv){
    if(subtr > len/2){
        c++;
        subtr-=n;
    }
   }
    return c;
}
};