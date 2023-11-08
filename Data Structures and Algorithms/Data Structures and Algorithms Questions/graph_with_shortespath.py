import heapq
import collections


def shortespath(edges,node1,node2):
    """
    finds the shortest weighted path with given values(edges,starting node = node1,target node = node2)
    """

    def builtgraph(edges):
        """
        converts edges to an adjacency list.
        """
        graph = collections.defaultdict(list)
        for key in edges:
            fro, to, weight = edges[key]
            graph[fro].append((to,weight))
        return graph
    
    graph = builtgraph(edges)
    heap = [(0,node1)] # initialize the heap with  cost and starting node 
    visited = set() # keeps track of the nodes to prevent infinite cycles.
    path = [] # stores the nodes that make up the shortest path

    while heap:
        cost, node = heapq.heappop(heap)
        visited.add(node)
        path.append(node)

        if node == node2:
            """
            if the current node equals to the target node, returns the total cost and the path
            """
            return [path,cost]
        
        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                """
                total cost = current cost + weight
                """
                heapq.heappush(heap,(cost + weight, neighbour)) #pushes the total cost for the neighbour and the neighbour itself
    
    return -1 # if there is no node that meets target node returns -1


edges = {"1001": [1, 2, 10], "1002": [2, 3, 15], "1003": [1, 3, 5], "1004": [2, 4, 8], "1005": [3, 4, 3]}
print(shortespath(edges,1,4))
