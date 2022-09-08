class Solution:
    # O(V + E) time | O(V) space
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.constructGraph(prerequisites)

        for i in range(numCourses):
            if not self.dfs(i, set(), set(), graph):
                return False

        return True


    def dfs(self, course, visiting, visited, graph):
        if course in visiting:
            return False
        if course in visited:
            return True

        visiting.add(course)

        for c in graph[course]:
            if not self.dfs(c, visiting, visited, graph):
                return False

        visiting.remove(course)
        visited.add(course)

        return True


    def constructGraph(self, prereq):
        graph = defaultdict(list)

        for a, b in prereq:
            graph[a].append(b)

        return graph