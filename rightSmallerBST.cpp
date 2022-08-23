using namespace std;
#include <vector>

class SpecialBST {
public:
  int value;
  int leftSubtreeSize;
  SpecialBST *left;
  SpecialBST *right;
  
  SpecialBST(int value) {
    this->value = value;
    leftSubtreeSize = 0;
    left = nullptr;
    right = nullptr;
  }

  void insert(int value, int idx, vector<int> &rightSmaller, int numSmaller = 0) {
    if (value < this->value) {
      leftSubtreeSize++;
      if (left == nullptr) {
        left = new SpecialBST(value);
        rightSmaller[idx] = numSmaller;
      }
      else {
        left->insert(value, idx, rightSmaller, numSmaller);
      }
    }
    else {
      numSmaller += leftSubtreeSize;
      if (value > this->value) 
        numSmaller++;
      if (right == nullptr) {
        right = new SpecialBST(value);
        rightSmaller[idx] = numSmaller;
      }
      else {
        right->insert(value, idx, rightSmaller, numSmaller);
      }
    }
  }
  
};

vector<int> rightSmallerThan(const vector<int>& arr) {
  
  if (arr.size() == 0) {
    return {}; 
  }
  
  vector<int> ret_val = arr;
  int lastIdx = arr.size() - 1;
  SpecialBST *bst = new SpecialBST(arr[lastIdx]);
  ret_val[lastIdx] = 0;
  for (int i = arr.size() - 2; i >= 0; --i) {
     bst->insert(arr[i], i, ret_val); 
  }
  
  return ret_val;
}
