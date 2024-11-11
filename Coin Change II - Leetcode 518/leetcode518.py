#  Problem: Coin Change II - Leetcode 518
# Problem link: https://leetcode.com/problems/coin-change-II/
# Difficulty: Medium
# Date : 11/10/2024

# Problem Understanding:

# We have an amount and a list of coins.
# We need to return the number of combinations that make up that amount.
# We can use each coin an unlimited number of times.
# The input is the amount and a list of coins.
# The output is the number of combinations.

# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: There are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: The amount of 3 cannot be made up by 2.

# Algorithm: 

# Knapsack Problem - Dynamic Programming 
# resources: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/#

# It is a knapsack problem because we have a target amount and a list of coins. 
# The coins can be used multiple times. 

# Approach:

# 1 - Create a dp array of size amount + 1 and initialize it with 0.
# The dp array will store the number of ways to make up the amount using the coins.
# The index of the dp array represents the amount.   

# 2. Setting the Base case:
# The dp[0] is initialized to 1 because there is only one way to make up the amount of 0.
# That is by not choosing any coin.

# 3 - Iterate through the coins and update the dp array. 
#  For each amount from the coin value to the target amount,
#  add the number of ways to make up the amount using the coin.
#  The number of ways to make up the amount is the sum of the number of ways to make up the amount - coin value.

# 4 - Return the number of ways to make up the target amount.
# the final result is stored in the dp array at the target amount.

# Code :

from typing import List

class Solution:
       def change(self, amount: int, coins: List[int]) -> int:
                  # Initialize the dp array with 0 and size amount + 1
                  dp = [0] * (amount + 1)
                  # Base case
                  dp[0] = 1   
                  # Iterate through the coins
                  for coin in coins:
                        # Update the dp array when the coin is less than or equal to the amount
                        for i in range(coin, amount + 1):
                        # The number of ways to make up the amount is the sum of the number of ways to make up the amount - coin value.
                              dp[i] += dp[i - coin]
                  # Return the number of ways to make up the target amount.
                  return dp[amount] 
       
       
# Time complexity: O(amount * len(coins))
# Space complexity: O(amount)


                        












