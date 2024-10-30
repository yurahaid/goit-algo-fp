import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=12)
G.add_edge('D', 'E', weight=4)
G.add_edge('D', 'E', weight=4)
G.add_edge('E', 'F', weight=7)
G.add_edge('E', 'j', weight=3)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()


def dijkstra(graph: nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

# використовуємо heapq для зберігання вершин які потрібно відвідати і обирати в першу чергу куди веде найменша відстань
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # якщо вже відвали дану вершину і відстань була коротшою
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            distance = distances[current_vertex] + graph[current_vertex][neighbor]['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Виклик функції для вершини A
print(dijkstra(G, 'A'))
