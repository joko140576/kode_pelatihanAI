import tkinter as tk
from tkinter import messagebox

# Definisikan graf sebagai dictionary
graph = {
    'A': ['B', 'C'],  # A terhubung langsung dengan B dan C
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start, end, path=[]):
    path = path + [start]  # Tambahkan lokasi saat ini ke jalur yang telah dilalui

    if start == end:  # Jika mencapai lokasi tujuan
        return path  # Kembalikan jalur yang ditemukan

    if start not in graph:  # Jika lokasi tidak ada di graf
        return None

    for neighbor in graph[start]:  # Telusuri semua tetangga
        if neighbor not in path:  # Jika tetangga belum dikunjungi
            new_path = dfs(graph, neighbor, end, path)  # Lakukan DFS rekursif
            if new_path:  # Jika jalur ditemukan
                return new_path  # Kembalikan jalur yang ditemukan

    return None  # Jika tidak ada jalur yang ditemukan

def draw_graph(canvas, path):
    canvas.delete("all")  # Bersihkan canvas sebelumnya

    # Koordinat untuk menggambar node
    coordinates = {
        'A': (150, 50),
        'B': (50, 150),
        'C': (250, 150),
        'D': (30, 250),
        'E': (100, 250),
        'F': (200, 250)
    }

    # Gambar semua node
    for node, (x, y) in coordinates.items():
        canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue')
        canvas.create_text(x, y, text=node)

    # Gambar sisi
    for node, neighbors in graph.items():
        x1, y1 = coordinates[node]
        for neighbor in neighbors:
            x2, y2 = coordinates[neighbor]
            canvas.create_line(x1, y1, x2, y2)

    # Gambar rute terbaik
    if path:
        for i in range(len(path) - 1):
            x1, y1 = coordinates[path[i]]
            x2, y2 = coordinates[path[i + 1]]
            canvas.create_line(x1, y1, x2, y2, fill='red', width=3)

def draw_initial_map(initial_canvas):
    initial_canvas.delete("all")  # Bersihkan canvas sebelumnya

    # Koordinat untuk menggambar node awal
    coordinates = {
        'A': (150, 50),
        'B': (50, 150),
        'C': (250, 150),
        'D': (30, 250),
        'E': (100, 250),
        'F': (200, 250)
    }

    # Gambar semua node
    for node, (x, y) in coordinates.items():
        initial_canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightgray')
        initial_canvas.create_text(x, y, text=node)

    # Gambar sisi
    for node, neighbors in graph.items():
        x1, y1 = coordinates[node]
        for neighbor in neighbors:
            x2, y2 = coordinates[neighbor]
            initial_canvas.create_line(x1, y1, x2, y2, fill='lightgray')

def find_route():
    start = entry_start.get()
    end = entry_end.get()
    path = dfs(graph, start, end)

    if path:
        messagebox.showinfo("Rute Ditemukan", "Rute: " + " -> ".join(path))
        draw_graph(canvas, path)
    else:
        messagebox.showwarning("Rute Tidak Ditemukan", "Tidak ada rute dari {} ke {}".format(start, end))

# Setup Tkinter window
root = tk.Tk()
root.title("Pencarian Rute Menggunakan DFS")

# Frame untuk canvas
frame = tk.Frame(root)
frame.pack(pady=20)

# Canvas untuk graf hasil
canvas = tk.Canvas(frame, width=400, height=400, bg='white')
canvas.pack(side=tk.RIGHT)

# Canvas untuk peta awal
initial_canvas = tk.Canvas(frame, width=400, height=400, bg='white')
initial_canvas.pack(side=tk.LEFT)

# Gambar peta awal
draw_initial_map(initial_canvas)

# Input untuk lokasi awal dan tujuan
tk.Label(root, text="Lokasi Awal:").pack()
entry_start = tk.Entry(root)
entry_start.pack()

tk.Label(root, text="Lokasi Tujuan:").pack()
entry_end = tk.Entry(root)
entry_end.pack()

# Tombol untuk mencari rute
button_find = tk.Button(root, text="Cari Rute", command=find_route)
button_find.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
