# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance- LeetCode 1334
# Problem link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# Difficulty: Medium
# Date : 11/7/2024

# Problem Understanding:

# We have n cities number from 0 to n-1
# List of edges from i to to i and weight i
# weight i is the threshold distance between from i to to i.
# We need to return smallest city number at most threshold distance 
# If we have Multiple cities we are returning city with greatest number 

# Example 1:
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3
# Explanation: The figure above describes the graph.
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2]
# City 1 -> [City 0, City 2, City 3]
# City 2 -> [City 0, City 1, City 3]
# City 3 -> [City 1, City 2]
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, 
# but we have to return city 3 since it has the greatest number.

# Example 2:
# Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
# Output: 0
# Explanation: The figure above describes the graph.
# The neighboring cities at a distanceThreshold = 2 for each city are:
# City 0 -> [City 1]
# City 1 -> [City 0, City 4]
# City 2 -> [City 3, City 4]
# City 3 -> [City 2, City 4]
# City 4 -> [City 1, City 2, City 3]
# The city 0 has 1 neighboring city at a distanceThreshold = 2.



# Algorithm: 

# Floyd-Warshall Algorithm
# Floyd-Warshall Algorithm is used to find the shortest path between all pairs of vertices in a weighted graph.
# Resources:https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

# Other Approach: using Dijkstra's Algorithm greedy approach
# Dijkstra's Algorithm is used to find the shortest path between the source node and all other nodes in the graph.
# Resources:https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Floyd-warshall Algorithm is better in this case because the number of cities is small and the distance threshold is small.
# Compared to Dijkstra's Algorithm which is better for large graphs.


# Step 1: Initialize the distance matrix with infinity
# Step 2: Distance from city to itself is 0
# Step 3: Add the initial distance based on the edges
# Step 4: Floyd-Warshall Algorithm to compute Shortest Path between all pairs 
# Step 5: Count the reachable cities within the threshold for each city
# step 6: update the result city based on the minimum neighbors with tie breaker as the greatest city number

# Code :    

class Solution:
      def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
            # Step 1: Initialize the distance matrix with infinity
            # n is the number of cities and float('inf') is infinity value as the initial distance for the cities
            # distance is the matrix to store the distance between the cities and k
            # *n is used to create a 2D matrix with n rows and n columns
            distance = [[float('inf')] * n for _ in range(n)]
            
            # Step 2: Distance from city to itself is 0
            # Initialize the diagonal with 0 because the distance from the city to itself is 0
            # For example, the distance from city 0 to city 0 is 0
            for i in range(n):
                  distance[i][i] = 0
            
            # Step 3: Add the initial distance based on the edges
            # u, v, w are the edges from u to v with weight w
            for u, v, w in edges:
                  distance[u][v] = w
                  distance[v][u] = w
            
            # Step 4: Floyd-Warshall Algorithm to compute Shortest Path between all pairs
            # The distance matrix is updated with the shortest path between the cities
            # The shortest path is computed using the Floyd-Warshall Algorithm
            for k in range(n): # Intermediate node between i and j
                  for i in range(n): # Source node
                        for j in range(n): # Destination node
                              distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) # Update the distance matrix
            
            # Step 5: Count the reachable cities within the threshold for each city
            # Initialize the count to 0 for each city
            # The count is the number of reachable cities within the threshold distance for each city
            min_neighbors = float('inf') # Initialize the minimum neighbors to infinity
            result_city = -1 # Initialize the result city to -1

            for city in range(n): # Iterate through each city
                  count = sum(1 for j in range(n) if distance[city][j] <= distanceThreshold and city != j)
                   
            # Step 6: update the result city based on the minimum neighbors with tie breaker as the greatest city number
                  if count <= min_neighbors:
                        min_neighbors = count
                        result_city = city
            return result_city





            
            
