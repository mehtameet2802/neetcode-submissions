class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for node,w in zip(equations,values):
            u = node[0]
            v = node[1]
            graph[u].append((v,w))
            graph[v].append((u,1/w))
        
        ans = []

        def helper(s,e):
            queue = deque([(s,1)])
            visited = set()

            while queue:

                ele,w = queue.popleft()
                visited.add(ele)

                if ele == e:
                    return w

                for nei, nw in graph[ele]:
                    if nei not in visited:
                        queue.append((nei,w*nw))

            return float(-1)

        for u,v in queries:
            if u not in graph or v not in graph:
                ans.append(float(-1))
            elif u == v:
                ans.append(float(1))
            else:
                ans.append(helper(u,v))

        return ans
