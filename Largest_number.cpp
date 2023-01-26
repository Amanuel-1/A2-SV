class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.rbegin(),nums.rend(),[](auto a, auto b){
           if(to_string(a).size() ==to_string(b).size()){
               return b>a;
           }
       
           else{
               return to_string(b)+to_string(a)>to_string(a)+to_string(b) ;
               }
             });

             string ans;
    for(auto v : nums){
        ans+=to_string(v );
    }
    return (ans[0]=='0')?"0":ans ;
    }
   
};
