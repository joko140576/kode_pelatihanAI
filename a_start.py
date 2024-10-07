import tkinter as tk
from tkinter import messagebox
import heapq
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name  # Nama node
        self.parent = parent  # Node orang tua
        self.g = g  # Biaya dari start node ke node ini
        self.h = h  # Estimasi biaya dari node ini ke tujuan
        self.f = g + h  # Total biaya (g + h)

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal, graph, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_set:
                continue

            g_cost = current_node.g + cost
            h_cost = heuristic[neighbor]
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

            if neighbor_node in open_set:
                continue

            heapq.heappush(open_set, neighbor_node)

    return None

def draw_graph(path=None):
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'E': 1},
        'D': {'B': 2, 'E': 1},
        'E': {'B': 5, 'C': 1, 'D': 1},
    }

    plt.figure(figsize=(8, 5))

    # Menggambar semua tepi graf
    for node, edges in graph.items():
        for neighbor, cost in edges.items():
            plt.plot([ord(node) - 65, ord(neighbor) - 65], [0, 0], 'ko-')
            plt.text((ord(node) - 65 + ord(neighbor) - 65) / 2, 0.05, f"{cost}", ha='center')

    if path:  # Jika ada jalur yang ditemukan
        path_indices = [ord(n) - 65 for n in path]
        plt.plot(path_indices, [0] * len(path_indices), 'ro-', label='Path')

    plt.xticks(range(len(graph)), graph.keys())
    plt.yticks([])
    plt.title('A* Path Finding')
    if path:
        plt.legend()
    plt.grid()
    plt.show()

def find_path():
    start_node = entry_start.get().strip()
    goal_node = entry_goal.get().strip()

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'E': 1},
        'D': {'B': 2, 'E': 1},
        'E': {'B': 5, 'C': 1, 'D': 1},
    }

    heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 0,
    }

    # Gambarkan graf awal
    draw_graph()

    path = a_star(start_node, goal_node, graph, heuristic)

    if path:
        messagebox.showinfo("Jalur Terpendek", f"Jalur terpendek dari {start_node} ke {goal_node}: {' -> '.join(path)}")
        draw_graph(path)
    else:
        messagebox.showerror("Kesalahan", f"Tidak ada jalur yang ditemukan dari {start_node} ke {goal_node}.")

# Antarmuka Pengguna
root = tk.Tk()
root.title("A* Path Finder")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_start = tk.Label(frame, text="Node Awal (A, B, C, D, E):")
label_start.grid(row=0, column=0, padx=5, pady=5)

entry_start = tk.Entry(frame)
entry_start.grid(row=0, column=1, padx=5, pady=5)

label_goal = tk.Label(frame, text="Node Tujuan (A, B, C, D, E):")
label_goal.grid(row=1, column=0, padx=5, pady=5)

entry_goal = tk.Entry(frame)
entry_goal.grid(row=1, column=1, padx=5, pady=5)

button_find = tk.Button(frame, text="Cari Jalur", command=find_path)
button_find.grid(row=2, columnspan=2, pady=10)

root.mainloop()
