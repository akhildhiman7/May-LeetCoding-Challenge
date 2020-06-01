/*
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
*/

class Solution {
public:

    int helper(string word1, string word2, int i, int j, int a, int b, vector<vector<int>> &dp) {
        if (i == a and j == b) return 0;
        if (i == a) return b-j;
        if (j == b) return a-i;

        if (dp[i][j] != -1) return dp[i][j];

        if (word1[i] == word2[j])
            return helper(word1, word2, i+1, j+1, a, b, dp);

        int aa, bb, cc;

        aa = helper(word1, word2, i, j+1, a, b, dp); //insert
        bb = helper(word1, word2, i+1, j, a, b, dp); //delete
        cc = helper(word1, word2, i+1, j+1, a, b, dp); //replace

        dp[i][j] = min(aa, min(bb, cc)) + 1;
        return dp[i][j];
    }

    int minDistance(string word1, string word2) {
        int a = word1.length(), b = word2.length();
        vector<vector<int>> dp(a, vector<int>(b, -1));

        return helper(word1, word2, 0, 0, word1.length(), word2.length(), dp);
    }
};
