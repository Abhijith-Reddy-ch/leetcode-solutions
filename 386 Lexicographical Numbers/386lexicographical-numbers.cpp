class Solution {
public:
    std::vector<int> lexicalOrder(int n) {
        std::vector<std::string> str_numbers;

        for (int i = 1; i <= n; ++i) {
            str_numbers.push_back(std::to_string(i));
        }

        std::sort(str_numbers.begin(), str_numbers.end());
        
        std::vector<int> result;
        for (const std::string& str : str_numbers) {
            result.push_back(std::stoi(str));
        }
        
        return result;
    }
};