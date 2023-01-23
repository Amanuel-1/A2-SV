/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* t1 = head ;
        if(head==nullptr ||head->next==nullptr)return head ;
         ListNode* t2 =t1->next ;
      //  for(;n->next!=nullptr; n = n->next){
          while(t2!=nullptr){
           if(t1->val==t2->val){
               t2 = t2->next ;
               t1->next = t2 ; 
           }
          else{
              t1 = t2 ;
              t2 = t2->next ; 

          }
             //  n = n->next;
           
        
          }
        //  cout <<head->val;
           return head ; 
    }
};
