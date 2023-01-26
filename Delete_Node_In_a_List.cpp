/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* t = node , *r ; 
        int temp ; 
        while(t->next!=nullptr){
            temp = t->val ; 
            t->val = t->next->val ; 
            t->next->val = temp ;
            r = t ;
            t = t->next;
        }
       r->next = nullptr;
    }
};
