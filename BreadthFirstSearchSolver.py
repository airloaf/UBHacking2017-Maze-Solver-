
def bfs(graph, visited, queue, parent):
    current = queue[0]
    queue.pop(0)
    visited.append(current)

    neighbors = graph[current]

    for neighbor in neighbors:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
            parent[neighbor] = current

    if len(queue) > 0:
        bfs(graph, visited, queue, parent)
    else:
        return


def get_queued_nodes(graph, start, end):

    visited = []
    queue = []
    parent = {}

    queue.append(start)
    parent[start] = None

    bfs(graph, visited, queue, parent)

    nodeQueue = []

    par = end
    while par != None:
        nodeQueue.insert(0, par)
        par = parent[par]

    return nodeQueue
