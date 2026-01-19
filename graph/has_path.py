# def has_path(graph, src, dst):
#     if src == dst:
#         return True

#     for neighbor in graph[src]:
#         if has_path(graph, neighbor, dst) is True:
#             return True

#     return False

from collections import deque


# def has_path(graph, src, dst):
#   queue = deque([src])

#   while len(queue) > 0:
#     current = queue.popleft()
#     if current == dst:
#       return True
#     for neighbor in graph[current]:
#       queue.append(neighbor)

#   return False


def has_path(graph, src, dst):
    queue = deque([src])
    while len(queue) > 0:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

has_path(graph, "f", "j")  # False


def test_1():
    graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}
    assert has_path(graph, "f", "j") is False