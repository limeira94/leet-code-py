# def depth_first(graph, source):
#     stack = [source]
#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor)
            
            
def depth_first(graph, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
            
graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first(graph, 'a')

# a, b, d, f, c, e



"""  
LIFO
          values= a, b, d, f, c, e
------
stack
"""