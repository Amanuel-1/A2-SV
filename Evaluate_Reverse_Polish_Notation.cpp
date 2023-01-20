class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack ;
        int n1,n2 ;
         auto fun = [&](auto n2 , auto n1,auto e){
                if(e =="+"){
                    return (n2) +  (n1) ;
                }
                else if(e =="-"){
                    return (n2) -  (n1) ;
                }
                else if(e =="/"){
                    return (n2) /  (n1 );
                }
                else{
                    return (n2) *  (n1) ;
                }
            };
        for(auto e :tokens){
           
            if(e!="*" && e!="/" && e!="+" && e!="-" ){
                stack.push_back(stoi(e));
            }
            else{
                n1 = stack[stack.size()-1];
                n2 = stack[stack.size()-2];
               stack.pop_back();
               stack.pop_back(); 
               stack.emplace_back(fun(n2,n1,e));
            }
        }
        return stack[0];
    }
};
