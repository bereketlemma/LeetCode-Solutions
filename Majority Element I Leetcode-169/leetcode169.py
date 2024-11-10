# Problem: Majority Element I LeetCode 169
# Problem link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Date : 11/9/2024

# Problem Understanding:

# We have an array of integers.
# We need to return the majority element.
# The majority element is the element that appears more than n/2 times.
# The input is an array of integers.
# The output is the majority element.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Explanation: 3 appears more than n/2 times.

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# Explanation: 2 appears more than n/2 times.

# Algorithm: 

# two approaches: 

# 1. Using hashmap - the time complexity is O(n) and space complexity is O(n)
# 2. Using Boyer-Moore Voting Algorithm it is the best approach because 
# It requires only O(1) space complexity and O(n) time complexity.

# Hashmap Approach:

# Step 1: Initialize the hashmap - key as the element and value as the frequency
# Step 2: Iterate through the array and count the frequency of each element
# Step 3: Return the element with the frequency greater than n/2

# Code : Hashmap Approach
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            count = {} 
            for num in nums: 
                  if num in count: 
                        count[num]+=1 
                  else:
                        count[num]=1 
            for key in count: 
                  if count[key]>len(nums)//2: 
                        return key 
            return -1 

# Time complexity: O(n)
# Space complexity: O(n)


# Code: Boyer-Moore Algorithm

# How it works: 
# Boyer-moore algorithm works by canceling out each occurrence of an element e with all other elements that are not e.
# If the majority element exists, it will be the last element left in the end.


# Step 1: Initialize the count and candidate
# Step 2: Iterate through the array
# Step 3: If the count is 0, update the candidate
# Step 4: If the element is the candidate, increment the count
# Step 5: Else decrement the count
# Step 6: Return the candidate

from typing import List

class Solution:
      def majorityElement(self, nums: List[int]) -> int:
            count = 0
            candidate = None
            for num in nums:
                  if count == 0:
                        candidate = num
                  if num == candidate:
                        count += 1
                  else:
                        count -= 1
            return candidate
      
# Time complexity: O(n) 
# Space complexity: O(1)

