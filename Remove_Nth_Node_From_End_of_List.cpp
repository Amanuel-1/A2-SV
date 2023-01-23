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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *tr = head ; 
        int count = 0 ;
        while(tr !=nullptr){
             count++;
            tr = tr->next ;
           
        }
        tr = head ;
        if(count ==1)return nullptr ;
       if(count ==n)return  head->next;
        for(int i = 0 ; i<count-n-1 ; i++){
           tr = tr->next ; 
        }
        
       if(tr->next !=nullptr){
           tr->next = tr->next->next ;
       }
        cout << tr;
        return head ;
    }
};
