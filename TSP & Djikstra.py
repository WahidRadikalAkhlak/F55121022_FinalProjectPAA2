import networkx as nx
import time

def tsp(graph, start):
    def node_to_int(node):
        return ord(node) - ord('A')

    def int_to_node(num):
        return chr(num + ord('A'))

    n = graph.number_of_nodes()
    visited = [False] * n
    path = []
    path.append(start)
    visited[node_to_int(start)] = True
    total_weight = 0
    start_time = time.time()

    def tsp_util(curr):
        nonlocal total_weight
        min_weight = float('inf')
        next_node = None
        for neighbor in graph.neighbors(int_to_node(curr)):
            weight = graph[int_to_node(curr)][neighbor]['weight']
            if not visited[node_to_int(neighbor)] and weight < min_weight:
                min_weight = weight
                next_node = neighbor
        if next_node is not None:
            path.append(next_node)
            visited[node_to_int(next_node)] = True
            total_weight += min_weight
            tsp_util(node_to_int(next_node))

    tsp_util(node_to_int(start))
    end_time = time.time()
    return path, total_weight, end_time - start_time

def dijkstra(graph, start, end):
    dist = {}
    prev = {}
    unvisited = set(graph.nodes())
    start_time = time.time()

    def node_to_int(node):
        return ord(node) - ord('A')

    def int_to_node(num):
        return chr(num + ord('A'))

    for node in graph.nodes():
        dist[node] = float('inf')
    dist[start] = 0

    while unvisited:
        min_dist = float('inf')
        curr = None
        for node in unvisited:
            if dist[node] < min_dist:
                min_dist = dist[node]
                curr = node
        unvisited.remove(curr)

        for neighbor in graph.neighbors(curr):
            weight = graph[curr][neighbor]['weight']
            alt = dist[curr] + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = curr

    end_time = time.time()
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = prev[curr]
    path.append(start)
    path.reverse()
    return path, dist[end], end_time - start_time

def print_iterations(path):
    print("Iterasi:")
    for i, node in enumerate(path):
        print(f"Iterasi {i+1}: {node}")
    print()

def print_computation_time(time):
    print(f"Waktu Komputasi: {time:.6f} detik")

def print_shortest_path(path, weight):
    print("Jalur Terpendek TSP:")
    print(" -> ".join(path))
    print(f"Total Bobot: {weight}\n")

def main():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('A', 'C', weight=10)
    graph.add_edge('A', 'G', weight=12)
    graph.add_edge('B', 'A', weight=12)
    graph.add_edge('B', 'C', weight=8)
    graph.add_edge('B', 'D', weight=12)
    graph.add_edge('C', 'A', weight=10)
    graph.add_edge('C', 'B', weight=8)
    graph.add_edge('C', 'D', weight=11)
    graph.add_edge('C', 'E', weight=3)
    graph.add_edge('C', 'G', weight=9)
    graph.add_edge('D', 'C', weight=11)
    graph.add_edge('D', 'E', weight=11)
    graph.add_edge('D', 'F', weight=10)
    graph.add_edge('E', 'C', weight=3)
    graph.add_edge('E', 'D', weight=11)
    graph.add_edge('E', 'F', weight=6)
    graph.add_edge('E', 'G', weight=7)
    graph.add_edge('F', 'D', weight=10)
    graph.add_edge('F', 'E', weight=6)
    graph.add_edge('F', 'G', weight=9)
    graph.add_edge('G', 'A', weight=12)
    graph.add_edge('G', 'C', weight=9)
    graph.add_edge('G', 'E', weight=7)
    graph.add_edge('G', 'F', weight=9)

    while True:
        print("Pilihan Algoritma:")
        print("1. TSP (Traveling Salesman Problem)")
        print("2. Dijkstra")
        choice = int(input("Masukkan pilihan (1/2): "))
        if choice == 1:
            start_node = input("Pilih node Awal: ")
            tsp_path, tsp_weight, tsp_time = tsp(graph, start_node)
            print_iterations(tsp_path)
            print_computation_time(tsp_time)
            print_shortest_path(tsp_path, tsp_weight)
        elif choice == 2:
            start_node = input("Pilih node Awal: ")
            end_node = input("Pilih node Akhir(Node yang dituju): ")
            dijkstra_path, dijkstra_weight, dijkstra_time = dijkstra(graph, start_node, end_node)
            print_iterations(dijkstra_path)
            print_computation_time(dijkstra_time)
            print_shortest_path(dijkstra_path, dijkstra_weight)
        else:
            print("Pilihan tidak valid.")

        repeat = input("Lakukan pengurutan lagi? (y/n): ")
        if repeat.lower() != 'y':
            break

if __name__ == '__main__':
    main()