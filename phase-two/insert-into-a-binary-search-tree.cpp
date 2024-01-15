/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode * r =  root,*parent =nullptr;
        if(root ==nullptr){
            root  = new TreeNode(val);
            return root;
        }
        while(r){
            parent=r;
            if(r->val > val){
                r = r->left;
            }
            else{
            r =r->right;

            
            }
            
            
        }
        if(parent ==nullptr){
            if(root->val>val){
                root->left = new TreeNode(val);
            }
            else{
                root->right  =  new TreeNode(val);
            }
        }        
        else if(parent->val < val){
            parent->right = new TreeNode(val);
        }
        else{
            parent->left = new TreeNode(val);
        }

        return root;
    }
};