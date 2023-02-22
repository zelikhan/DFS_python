mygraph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'D': [],
    'C': ['E', 'F'],
    'E': [],
    'F': []
}

visited = []
queue = []


def mydfs(mygraph, visited, starting_node):
    if starting_node not in visited:
        print(starting_node, end=" ")
        visited.append(starting_node)

        for neighbour in mygraph[starting_node]:
            mydfs(mygraph, visited, neighbour)


print("Depth First Search Traversal : ")
mydfs(mygraph, visited, "A")
