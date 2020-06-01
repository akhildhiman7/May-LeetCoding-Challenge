'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        dik = {}
        for i in s:
            dik[i] = dik.get(i, 0) + 1
        temp = []
        for i, j in dik.items():
            temp.append([i, j])
        temp.sort(reverse = True, key = lambda x: x[1])
        result = ''
        for i in temp:
            result += i[0]*i[1]
        return result
