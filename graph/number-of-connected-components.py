from typing import List
class Solution:
	def numOfConnectedCom(self, n: int, edges: List[List[int]]) -> int:
		if n == 1:
			return 1
		adj = {node:[] for node in range(n)}
		component = 0
		for n1, n2 in edges:
			adj[n1].append(n2)
			adj[n2].append(n1)

		visit = set()

		def dfs(node):
			for nbr in adj[node]:
				if nbr not in visit:
					visit.add(nbr)
					dfs(nbr)

		for node in adj:
			if node in visit:
				continue
			else:
				visit.add(node)
				component += 1
				dfs(node)
		return component

print(Solution().numOfConnectedCom(6, [[0,1], [1,2], [2,3], [4,5]]))
