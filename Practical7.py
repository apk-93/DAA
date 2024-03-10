from sys import maxsize
from itertools import permutations
V=4
def TSP(graph,s):
    vertex=[]
    for i in range(V):
        vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)

    for perm in next_permutation:
        current_weigth=0
        k=s

        for j in range(V):
            current_weigth+=graph[k][perm[j]]
            k=perm[j]

        current_weigth+=graph[k][s]
        min_path=min(min_path,current_weigth)
    return min_path
if __name__=='__main__':
    graph=[[0,25,10,15],
           [25,0,10,45],
           [10,10,0,5],
           [15,45,5,0]]
    s=0
    print(TSP(graph,s))
     
