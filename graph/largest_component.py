from collections import deque
# def largest_component(graph):
#     visited = set()
#     longest = 0
#     for node in graph:
#         size = explore_size(graph, node, visited)
#         if size > longest:
#             longest = size

#     return longest

# def explore_size(graph, current, visited):
#     if current in visited:
#         return 0
#     visited.add(current)

#     size = 1

#     for neighbor in graph[current]:
#         size += explore_size(graph, neighbor, visited)

#     return size


def largest_component(graph):
    visited = set()
    largest = 0

    for node in graph:
        size = explore_size(graph, node, visited)
        print(size)
        if size > largest:
            largest = size

    return largest


def explore_size(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)

    size = 0
    queue = deque([node])
    while queue:
        current = queue.popleft()
        size += 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return size


largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4


