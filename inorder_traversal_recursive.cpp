
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Tree {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder_result;
        if (root == NULL) {
            return inorder_result;
        }
        inorder_result = inorderTraversal(root->left);
        inorder_result.push_back(root->val);
        auto right_inorder = inorderTraversal(root->right);
        inorder_result.insert(inorder_result.end(), right_inorder.begin(), right_inorder.end());
        return inorder_result;
    }
};
