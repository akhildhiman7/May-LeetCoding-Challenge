/*
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
*/

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> v;
        if (s.length() == 0) return v;
        int arr[26];
        memset(arr, 0, sizeof(arr));

        for (int i = 0; i < p.length(); i++) {
            arr[p[i] - 'a']++;
        }

        int left = 0, right = 0;
        int len = s.length(), count = p.length(), len2 = p.length();
        while (right < len) {
            if (arr[s[right++]-'a']-- > 0) count--;

            if (count == 0) v.push_back(left);

            if (right - left == len2 && arr[s[left++]-'a']++ > -1) count++;

        }
        return v;
    }
};
