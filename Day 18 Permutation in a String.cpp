/*
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
*/

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int arr[26]= {0};
        int left = 0, right = 0, len2 = s1.length(), len1 = s2.length(), count = s1.length();
        for (int i = 0; i < len2; i++)
            arr[s1[i]-'a'] += 1;
        while (right < len1) {
            if (arr[s2[right++] - 'a']-- > 0) count--;

            if (count == 0) return true;

            if (right - left == len2 and arr[s2[left++] - 'a']++ > -1) count++;
        }
        return false;
    }
};
