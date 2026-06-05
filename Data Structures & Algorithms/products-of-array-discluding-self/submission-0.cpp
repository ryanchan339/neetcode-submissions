class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> vect(nums.size(), 1);
        int product = 1;
        vector<int> prefix(nums.size(), 1);
        vector<int> suffix(nums.size(), 1);
        prefix[0] = nums[0];
        suffix[nums.size() - 1] = nums[nums.size() - 1];
        for (int i = 1; i < nums.size(); ++i) {
            prefix[i] = prefix[i - 1] * nums[i];
        }
        for (int i = nums.size() - 2; i >= 0; --i) {
            suffix[i] = suffix[i + 1] * nums[i];
        }
        vect[0] = suffix[1];
        for (int i = 1; i < nums.size() - 1; ++i) {
            vect[i] = prefix[i - 1] * suffix[i + 1];
        }
        vect[nums.size() - 1] = prefix[nums.size() - 2];
        return vect;
    }
};