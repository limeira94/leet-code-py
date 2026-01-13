
def undirected_path(edges, nodea, nodeb):
    graph = build_graph(edges)
    visited = set()
    return has_path(graph, nodea, nodeb, visited)

def has_path(graph, src, dst, visited):
    if visited in src:
        return False
    
    if (src == dst):
        return True
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) is True:
            return True
    
    return False

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