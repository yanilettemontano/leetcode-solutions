class Solution {
private:
vector <int> sol;
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        size_t len = nums.size();
        unordered_map <int, int> hash;

        for(int i = 0; i < len; i++){
            int secInt = target - nums.at(i);
            if(hash.find(secInt) != hash.end()){
                sol.push_back(i);
                sol.push_back(hash.find(secInt)->second);
                break;
            } else{
                hash[nums.at(i)] = i;
            }
        }
        return sol;
    }
};