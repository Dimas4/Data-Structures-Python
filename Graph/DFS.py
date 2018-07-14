def DFS(vertex, G, used):
    used.add(vertex)
    for i in G[vertex]:
        if i not in used:
            DFS(i, G, used)
