import sys
import time
import itertools


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_edge(self, start, end, weight):
        self.vertices.add(start)
        self.vertices.add(end)
        if start not in self.edges:
            self.edges[start] = {}
        self.edges[start][end] = weight


def tsp(graph, start, end):
    start_time = time.time()
    all_paths = []
    shortest_path = None
    shortest_distance = sys.maxsize

    all_permutations = itertools.permutations(graph.vertices)

    for permutation in all_permutations:
        if permutation[0] != start or permutation[-1] != end:
            continue

        distance = 0
        path = []
        for i in range(len(permutation) - 1):
            current_vertex = permutation[i]
            next_vertex = permutation[i + 1]

            if next_vertex in graph.edges[current_vertex]:
                distance += graph.edges[current_vertex][next_vertex]
                path.append(current_vertex)

        path.append(next_vertex)

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

        all_paths.append((path, distance))

    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, shortest_distance, all_paths, execution_time


def dijkstra(graph, start, end):
    start_time = time.time()
    distances = {}
    previous_vertices = {}
    unvisited_vertices = graph.vertices.copy()

    for vertex in graph.vertices:
        distances[vertex] = sys.maxsize
        previous_vertices[vertex] = None
    distances[start] = 0

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])

        if current_vertex == end:
            break

        unvisited_vertices.remove(current_vertex)

        for neighbor in graph.edges[current_vertex]:
            alternative_distance = distances[current_vertex] + graph.edges[current_vertex][neighbor]

            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance
                previous_vertices[neighbor] = current_vertex

    shortest_path = []
    current_vertex = end

    while current_vertex is not None:
        shortest_path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, distances[end], distances, execution_time


def print_path(path, distance):
    if path:
        print("Shortest Path:", " -> ".join(path))
        print("Total jarak:", distance)
    else:
        print("Path tidak ditemukan.")


def print_all_paths(all_paths, start, end):
    filtered_paths = [(path, distance) for path, distance in all_paths if path[0] == start and path[-1] == end]

    for path, distance in filtered_paths:
        print("Path:", " -> ".join(path))
        print("Jarak:", distance)
        print()


graph = Graph()
graph.add_edge('A', 'B', 12)
graph.add_edge('A', 'C', 10)
graph.add_edge('A', 'G', 12)
graph.add_edge('B', 'C', 8)
graph.add_edge('B', 'D', 12)
graph.add_edge('C', 'D', 11)
graph.add_edge('C', 'E', 3)
graph.add_edge('C', 'G', 9)
graph.add_edge('D', 'C', 11)
graph.add_edge('D', 'E', 11)
graph.add_edge('D', 'F', 10)
graph.add_edge('E', 'G', 7)
graph.add_edge('E', 'F', 6)
graph.add_edge('G', 'A', 12)
graph.add_edge('G', 'C', 9)
graph.add_edge('G', 'E', 7)
graph.add_edge('G', 'F', 9)

algorithm = input("Ketikkan algorithm yang ingin digunakan ([1]TSP / [2]Dijkstra): ")

if algorithm == "1":
    start = input("Masukkan vertex awal: ")
    end = input("Masukkan vertex tujuan: ")

    shortest_path, shortest_distance, all_paths, execution_time = tsp(graph, start, end)

    print("\nHasil TSP:")
    print("-------------")
    print("Shortest Path:")
    print_path(shortest_path, shortest_distance)
    print("\nAll Paths:")
    print_all_paths(all_paths, start, end)
    print("Waktu eksekusi:", execution_time, "seconds")

elif algorithm == "2":
    start = input("Masukkan vertex awal: ")
    end = input("Masukkan vertex tujuan: ")

    shortest_path, shortest_distance, distances, execution_time = dijkstra(graph, start, end)

    print("\nHasil Dijkstra:")
    print("-----------------")
    print_path(shortest_path, shortest_distance)
    print("\nJarak:")
    for vertex, distance in distances.items():
        print(f"Jarak dari {start} ke {vertex}: {distance}")
    print("Waktu eksekusi:", execution_time, "seconds")

else:
    print("Pilihan tidak valid!.")
