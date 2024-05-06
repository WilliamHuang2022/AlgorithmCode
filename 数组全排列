#include <iostream>
#include <vector>
#include <string>
using namespace std;
int func(vector<int> nums, vector<int> semiproduct, vector<int> occupy,
             vector<vector<int>>& store) {//得出全排列的结果存放在store里面
        int n = occupy.size();
        for (int i = 0; i < n; i++) {
            if (occupy[i] == 0) {
                semiproduct.push_back(nums[i]);
                occupy[i] = 1; // 占用后向下生长
                if (semiproduct.size() == n) {
                    store.push_back(semiproduct);
                    return 1;
                }
                func(nums, semiproduct, occupy, store);
                occupy[i] = 0; // 让出位置
                semiproduct.pop_back();
            }
        }
        return 1;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> store; // 保存穷举的结果
        vector<int> semiproduct;
        vector<int> occupy(n, 0);
        func(nums, semiproduct, occupy, store);
        return store;
    }
