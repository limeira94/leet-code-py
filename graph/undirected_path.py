from collections import deque

# def undirected_path(edges, nodea, nodeb):
#     graph = build_graph(edges)
#     visited = set()
#     return has_path(graph, nodea, nodeb, visited)

# def has_path(graph, src, dst, visited):
#     if src in visited:
#         return False

#     if (src == dst):
#         return True

#     visited.add(src)

#     for neighbor in graph[src]:
#         if has_path(graph, neighbor, dst, visited) is True:
#             return True

#     return False


def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


def undirected_path_bfs(edges, node_a, node_b):
    graph = build_graph(edges)
    return has_path_bfs(graph, node_a, node_b)


def has_path_bfs(graph, src, dst):
    queue = deque([src])
    visited = set()

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

undirected_path_bfs(edges, "j", "m")
