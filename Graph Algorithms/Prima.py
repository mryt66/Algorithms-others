from setuptools.namespaces import flatten
def find(graph):
    graphm = max(flatten(graph)) 
    vertc = len(graph)  
    vertf = [False] * vertc  
    edges_found = 0  
    mst = 0
    vertf[0] = True  
    

    while edges_found < vertc - 1: 
        minimum_edge = graphm
        vertex_from = 0
        vertex_to = 0
        for i in range(vertc):
            if vertf[i]:
                for j in range(vertc):  
                    if (not vertf[j]) and graph[i][j]:
                        if minimum_edge > graph[i][j]:
                            minimum_edge = graph[i][j]
                            vertex_to = j  
                            vertex_from = i
                            
        print(vertex_from, " - ", vertex_to, " odleglosc: ", graph[vertex_from][vertex_to])
        vertf[vertex_to] = True
        mst += graph[vertex_from][vertex_to]
        edges_found += 1
    return mst

graph = [
    [0, 0, 1, 0, 0],
    [0, 2, 5, 4, 0],
    [3, 10, 0, 2, 0],
    [0, 0, 12, 0, 1],
    [1, 0, 6, 0, 0],
]

print("Minimalne drzewo:", find(graph))  