import sys
def show(dist):
    print("Wierzchołek -> Odległość")
    for index in range(len(dist)):
        print(str(index), "->", dist[index])

def close(dist, found):
    mindist = sys.maxsize

    for i in range(len(dist)):
        if dist[i] < mindist and found[i] is False:
            mindist = dist[i]
            min = i
    return min

def Dijikstra(head, graph):
    found = [False] * len(graph) 
    dist = [sys.maxsize] * len(graph) 
    dist[head] = 0      
    for _ in range(len(graph)):
        x = close(dist, found) 
        found[x] = True
        for y in range(len(graph)):
            if graph[x][y] > 0 and found[y] is False and dist[y] > dist[x] + graph[x][y]:
                dist[y] = graph[x][y]+dist[x]
    show(dist)
graph = [
    [0, 3, 1, 0, 0],
    [3, 0, 7, 5, 1],
    [1, 7, 0, 2, 0],
    [0, 5, 2, 0, 7],
    [0, 1, 0, 7, 0],
]
Dijikstra(head=2, graph=graph)