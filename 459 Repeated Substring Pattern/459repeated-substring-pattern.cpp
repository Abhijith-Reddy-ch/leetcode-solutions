class Solution {
public:
    bool repeatedSubstringPattern(string s) {
         string doubledString = s + s;
         size_t position = doubledString.find(s, 1);
         return position < s.size();
    }
};