"""
## Problem 3:
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

Time complexity : O(n)
Space complexity : O(n)
"""
def bijection (str1, str2):
    hash_map_s1 = dict()
    hash_map_s2 = dict()
    s1 = list(str1)
    s2 = str2.split(' ')
    if len(s1) != len(s2):
        return False
    for i,j in zip (s1,s2):
        if i not in hash_map_s1:
            hash_map_s1[i] = j
        else:
            if hash_map_s1[i] !=j:
                return False
        if j not in hash_map_s2:
            hash_map_s2[j] = i
        else:
            if hash_map_s2[j] !=i:
                return False
    return True
