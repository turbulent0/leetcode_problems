import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Example usage:

# Create a graph
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 4, 'E': 5},
    'C': {'F': 6},
    'D': {'G': 7},
    'E': {'G': 8, 'H': 9},
    'F': {'H': 10},
    'G': {},
    'H': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node + ":")
for node, distance in distances.items():
    print("Node:", node, "Distance:", distance)
