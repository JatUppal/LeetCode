from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        q = deque()
        for i in range(len(prerequisites)):
            indegree[prerequisites[i][0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        taken = 0
        while q:
            course = q.popleft()
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            taken += 1
        return taken == numCourses
        