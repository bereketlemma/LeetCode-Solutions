# Problem: Course Scheduler II :
# Problem link: https://leetcode.com/problems/course-schedule-ii/description/
# Difficulty: Medium
# Date : 11/5/2024


# Problem Understanding:

# We have number of courses to take, and a list of prerequisites.
# We need to return the order of courses to take, if it is possible.
# If it is not possible to take all the courses, return an empty list.
# The input is the number of courses and a list of prerequisites.
# The output is the order of courses to take.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: To take course 1 you should have finished course 0. 
# So the order of courses is [0,1]

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: []
# Explanation: There is a cycle in the graph, so it is impossible to take all courses.

# Algorithm: 

# Topological Sort
# Topological sort is way of ordering the vertices one by one in a directed graph.
# Directed graph is a graph where all the edges have a direction.
# Resources:https://www.geeksforgeeks.org/topological-sorting/#

# Approach:

# Using DFS:
# 1 - Create adjacency list for the prerequisites.
# 2 - Map each course to its prerequisites but first it was mapped to empty list.   
# 3 - A Course has 3 states : 0 - not visited, 1 - visited, 2 - visiting.
 
# Visited means the course is already taken. 
# Visiting means the course is being taken.
# Not visited means the course is not taken yet.

# 4 - Create an empty output list to store the order of courses to take.
# 5- Create a 2 list of sets, one for the visit and the other for the cycle.
# To check if a course is already visited or along the path of the cycle.

# 6 - create another function to do the DFS def dfs(course):
# 7 - if the course is in the cycle set, return False.      
# If the course is in the visit set, return True.

# 8 - Add the course to our cycle set to check if it is in the cycle.
# 9 - Go through every prerequisites of the course and do the DFS on them.
# 10 - If the DFS returns False, return False because there is a cycle.
# If the DFS returns True, then we are going to continue to go through the prerequisites.

# 11 - After the DFS, remove the course from the cycle set and add it to the visit set.
# Because we have already visited and it is no longer on the path of the cycle.

#12- Add the course to the visit set.
#13- Append the course to the output list.
#14- Return True.

# Code :

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prerequisites_map[course].append(pre)

        output = []
        visit = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in prerequisites_map[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output

# Complexity Analysis:

# Time Complexity: O(V+E)
# V is the number of courses and E is the number of prerequisites.  
# The time complexity of the DFS is O(V+E)
# Because we are going through all the courses and prerequisites.

# Space Complexity: O(V+E)
# The space complexity of the DFS is O(V+E)
# Because we are using the visit and cycle set to store the courses.
# The output list to store the order of courses to take.







