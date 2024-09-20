class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size();
        if (n == 0) return "";
        string combined = s + "#" + string(s.rbegin(), s.rend());
        int m = combined.size();
        vector<int> lps(m, 0);

        for (int i = 1; i < m; i++) {
            int j = lps[i - 1];
            while (j > 0 && combined[i] != combined[j]) {
                j = lps[j - 1];
            }
            if (combined[i] == combined[j]) {
                j++;
            }
            lps[i] = j;
        }

        int len = lps.back();
        string to_add = s.substr(len);
        reverse(to_add.begin(), to_add.end());
        return to_add + s;
    }
};

