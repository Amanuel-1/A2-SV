class Solution {
public:
    int hIndex(vector<int>& citations) {
        int bol=0 ;
        int i ;
        sort(citations.rbegin(),citations.rend());
      for(i=0;i<citations.size();i++){
         if(i<citations[i]){
             bol =max(bol,i);
         }
         else{break;}
         
      }  
      return i ;
    }
};
