"""
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"
Sorted s - aaccerr
sorted t - aaccerr

Output: true
Example 2:

Input: s = "jar", t = "jam"
sorted s - ajr
sorted t - ajm

using dic on S:     
value freq
j      1
a      1
r      1

using dic on t:
value freq
j      1
a      1
m      1

Time: O(s + t)
space: O(1)



Output: false

Example 3:
Input s = bored - 5 characher
input t = robed - 5 char 

sorted s = bdeor
sorted t = bdeor

return true-they are anagrams

Constraints:

s and t consist of lowercase English letters.
"""
# Using sorting Algo
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The two strings are not anagram if the len is not the same
        if len(t) != len(s):
            return False
        return sorted(s) == sorted (t)
# Time Complex : for length : O(t) + O(s)
# Time Complex : for Sorting : O(logt) + O(logs)
# Time Complex : Overall : O(tlogt) + O(slogs)
# Depeding on the sorting Algo used
# space Complexity: depends on what sorting Algo we're going to use 

# Using Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # init count vaibale and going through every char
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char not in count or count[char] == 0:
                count[char] += 1
            else:
                count[char] -= 1    
        return True      
# Time Complexity: O(s + t)
# Space Complexity: O(1) - as we're using a fixed size of 26 char
# Space Complexity: O(n) - if the char are not fixed



            






        
    
        

