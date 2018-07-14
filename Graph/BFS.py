from collections import deque


N, M = [int(i) for i in input().split()]
distance = [None] * N
graph = {i: set() for i in range(N)}
start_vertex = 0
queue = deque([start_vertex])
distance[start_vertex] = 0
parents = [None] * N


for i in range(M):
    v1, v2 = [int(i) for i in input().split()]
    graph[v1].add(v2)
    graph[v2].add(v1)

while queue:
    current = queue.popleft()
    for i in graph[current]:
        if distance[i] is None:
            distance[i] = distance[current] + 1
            parents[i] = current
            queue.append(i)

end_vertex = 9
path = [end_vertex]
parent = parents[end_vertex]
while parent is not None:
    path.append(parent)
    parent = parents[parent]


print(distance)
print(parents)
print(path[::-1])


