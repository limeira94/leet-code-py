
def largest_component(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > longest:
            longest = size
    
    return longest

def explore_size(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    
    size = 1
    
    for neighbor in graph[current]:
        size += explore_size(graph, neighbor, visited)
    
    return size