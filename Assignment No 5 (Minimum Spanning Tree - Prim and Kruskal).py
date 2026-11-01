import heapq

class Graph:
    def __init__(self):
        self.V = 0
        self.nodes = {}         # index -> building name
        self.node_indices = {}  # building name -> index
        self.graph = []         # Edge list for Kruskal
        self.adj_list = {}      # Adjacency list for Prim

    def add_building(self, name):
        if name in self.node_indices:
            print(f"Building '{name}' already exists.")
            return
        self.nodes[self.V] = name
        self.node_indices[name] = self.V
        self.adj_list[self.V] = []
        self.V += 1
        print(f"Building '{name}' added successfully.")

    def add_distance(self, b1, b2, distance):
        if b1 not in self.node_indices or b2 not in self.node_indices:
            print("One or both buildings not found.")
            return
        u = self.node_indices[b1]
        v = self.node_indices[b2]
        self.graph.append([u, v, distance])
        self.adj_list[u].append((v, distance))
        self.adj_list[v].append((u, distance))
        print(f"Distance of {distance} meters added between '{b1}' and '{b2}'.")

    def display_graph(self):
        print("\n--- Campus Map ---")
        for u in self.adj_list:
            building = self.nodes[u]
            print(f"{building} is connected to:")
            for v, w in self.adj_list[u]:
                print(f"  -> {self.nodes[v]} ({w} meters)")
        print()

    # --------- Kruskal’s Algorithm ---------
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, xroot, yroot):
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        total_weight = 0

        self.graph.sort(key=lambda x: x[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)
                e += 1
                total_weight += w

        print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
        for u, v, w in result:
            print(f"{self.nodes[u]} - {self.nodes[v]}: {w} meters")
        print("Total Distance:", total_weight, "meters")

    # --------- Prim’s Algorithm ---------
    def prim_mst(self):
        if self.V == 0:
            print("Graph is empty.")
            return

        visited = [False] * self.V
        min_heap = [(0, 0, -1)]  # (weight, current, parent)
        result = []
        total_weight = 0

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            if parent != -1:
                result.append((parent, u, weight))
                total_weight += weight
            for v, w in self.adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))

        print("\nMinimum Spanning Tree (Prim's Algorithm):")
        for u, v, w in result:
            print(f"{self.nodes[u]} - {self.nodes[v]}: {w} meters")
        print("Total Distance:", total_weight, "meters")

# ---------------------------
# Main Menu-Driven Program
# ---------------------------

def main():
    g = Graph()

    while True:
        print("\n--- College Campus Graph Menu ---")
        print("1. Add Building")
        print("2. Add Distance Between Buildings")
        print("3. Display Campus Map")
        print("4. Minimum Spanning Tree (Kruskal's Algorithm)")
        print("5. Minimum Spanning Tree (Prim's Algorithm)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter building name: ").strip()
            g.add_building(name)

        elif choice == '2':
            b1 = input("Enter first building name: ").strip()
            b2 = input("Enter second building name: ").strip()
            try:
                distance = int(input("Enter distance in meters: "))
                g.add_distance(b1, b2, distance)
            except ValueError:
                print("Invalid distance. Please enter an integer.")

        elif choice == '3':
            g.display_graph()

        elif choice == '4':
            g.kruskal_mst()

        elif choice == '5':
            g.prim_mst()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()