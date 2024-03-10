import collections

def bfs(graph,root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)

    while queue:
        vertex=queue.popleft()
        print(str(vertex)+" ",end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                

if __name__=='__main__':
    graph={1:[2,5],2:[1,3,5],3:[2,4,5],4:[3,5],5:[2,3,5]}
    print("BFS TRavesal")
    bfs(graph,1)

    
