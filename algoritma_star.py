import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Fungsi heuristik
def heuristic(a, b):
    return 0

# Fungsi A* untuk mencari rute termurah
def astar_cheapest_route(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_score = {start: 0}
    came_from = {}
    
    while open_list:
        current_cost, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], current_cost
        
        for neighbor, price in graph[current].items():
            tentative_g_score = g_score[current] + price
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current
    
    return None, float('inf')

# Fungsi untuk menggambar graf dengan tata letak seperti pohon
def draw_tree_graph(graph, path=None):
    G = nx.DiGraph()  # Menggunakan Directed Graph untuk tata letak pohon
    
    for node in graph:
        for neighbor, cost in graph[node].items():
            G.add_edge(node, neighbor, weight=cost)

    # Menggunakan tata letak manual untuk membuat struktur pohon
    pos = {
        'A': (0, 3), 'B': (-1, 2), 'C': (1, 2), 'D': (-1, 1), 'E': (1, 1), 'F': (0, 0)
    }
    labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight="bold", font_color="black")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)
    
    plt.title("Grafik Rute dalam Bentuk Pohon")
    plt.show()

# Fungsi untuk memproses input rute dari tkinter
def find_route():
    start = start_entry.get().upper()
    goal = goal_entry.get().upper()

    if start not in graph or goal not in graph:
        messagebox.showerror("Error", "Titik awal atau tujuan tidak ditemukan dalam graf.")
        return

    path, cost = astar_cheapest_route(graph, start, goal)
    if path:
        messagebox.showinfo("Rute Termurah", f"Rute: {' -> '.join(path)}\nTotal Biaya: {cost}")
        draw_tree_graph(graph, path)
    else:
        messagebox.showerror("Error", "Tidak ada rute ke tujuan.")

# Fungsi untuk menggambar graf awal
def draw_initial_tree_graph():
    draw_tree_graph(graph)

# Inisialisasi graf dengan biaya antar titik
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 4, 'E': 7},
    'C': {'A': 2, 'D': 8},
    'D': {'B': 4, 'C': 8, 'E': 6, 'F': 3},
    'E': {'B': 7, 'D': 6, 'F': 1},
    'F': {'D': 3, 'E': 1}
}

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Pencarian Rute Termurah A*")

# Label dan Input untuk titik awal
start_label = tk.Label(root, text="Titik Awal:")
start_label.grid(row=0, column=0, padx=10, pady=10)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1, padx=10, pady=10)

# Label dan Input untuk titik tujuan
goal_label = tk.Label(root, text="Titik Tujuan:")
goal_label.grid(row=1, column=0, padx=10, pady=10)
goal_entry = tk.Entry(root)
goal_entry.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk mencari rute
find_button = tk.Button(root, text="Cari Rute", command=find_route)
find_button.grid(row=2, columnspan=2, pady=10)

# Tombol untuk menampilkan graf awal
graph_button = tk.Button(root, text="Lihat Graf Awal", command=draw_initial_tree_graph)
graph_button.grid(row=3, columnspan=2, pady=10)

# Menjalankan loop utama Tkinter
root.mainloop()
